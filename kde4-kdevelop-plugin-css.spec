%define		orgname		css
%define		svnrev		1107713

Summary:	Upload plugin for kdevplatform
Summary(pl.UTF-8):	Wtyczka wysyłania dla kdevplatform
Name:		kde4-kdevelop-plugin-css
Version:	0.0.1
Release:	0.%{svnrev}.1
License:	GPL
Group:		X11/Development/Tools
# get it via: svn co svn://anonsvn.kde.org/home/kde/trunk/playground/devtools/kdevelop4-extra-plugins/css
Source0:	http://77.236.1.75/src/%{orgname}-svn-%{svnrev}.tar.bz2
# Source0-md5:	a0789d8db036a3cf4494934de025001a
URL:		http://www.kdevelop.org/
BuildRequires:	kde4-kdevplatform-devel >= 0.9.97
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CSS kdevelop plugin.

%description -l pl.UTF-8
Wtyczka CSS dla kdevelop.

%prep
%setup -q -n %{orgname}

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	../
%{__make}
cd ../

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kdevcsslanguagesupport.so
%attr(755,root,root) %{_libdir}/libkdev4cssparser.so
%{_datadir}/apps/kdevcsssupport
%{_datadir}/kde4/services/kdevcsssupport.desktop
