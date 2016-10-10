Summary:	C/C++ port of the Sass CSS precompiler
Name:		libsass
Version:	3.3.6
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/sass/libsass/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6bb2a93efb9802758ff7640ab69ce498
URL:		http://sass-lang.com/libsass
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsass is a C/C++ port of the Sass CSS precompiler. The original
version was written in Ruby, but this version is meant for efficiency
and portability.

This library strives to be light, simple, and easy to build and
integrate with a variety of platforms and languages.

Libsass is just a library, but if you want to RUN libsass, install the
sassc package.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsass.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Readme.md SECURITY.md LICENSE
%attr(755,root,root) %{_libdir}/libsass.so.*.*.*
%ghost %{_libdir}/libsass.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/sass.h
%{_includedir}/sass2scss.h
%{_includedir}/sass
%{_libdir}/libsass.so
%{_pkgconfigdir}/libsass.pc
