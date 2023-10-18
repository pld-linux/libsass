#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	C/C++ port of the Sass CSS precompiler
Summary(pl.UTF-8):	Port C/C++ prekompilatora CSS Sass
Name:		libsass
Version:	3.6.5
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/sass/libsass/releases
Source0:	https://github.com/sass/libsass/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c49765b9b3824dcd4a7423225ca28bad
URL:		https://sass-lang.com/libsass
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
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

%description -l pl.UTF-8
Libsass to port C/C++ prekompilatora CSS Sass. Pierwotna wersja
została napisana w języku Ruby, a ta powstała z myślą o wydajności i
przenośności.

Biblioteka stara się być lekka, prosta i łatwa do zbudowania oraz
integrowania z wieloma różnymi platformami i językami.

Libsass to tylko biblioteka - aby URUCHOMIĆ kompilator, należy
zainstalować pakiet sassc.

%package devel
Summary:	Development files for libsass
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libsass
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for developing applications
that use libsass.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę libsass.

%package static
Summary:	Static libsass library
Summary(pl.UTF-8):	Statyczna biblioteka libsass
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsass library.

%description static -l pl.UTF-8
Statyczna biblioteka libsass.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

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
%attr(755,root,root) %ghost %{_libdir}/libsass.so.1

%files devel
%defattr(644,root,root,755)
%doc docs/[!b]*.md
%attr(755,root,root) %{_libdir}/libsass.so
%{_includedir}/sass.h
%{_includedir}/sass2scss.h
%{_includedir}/sass
%{_pkgconfigdir}/libsass.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libsass.a
%endif
