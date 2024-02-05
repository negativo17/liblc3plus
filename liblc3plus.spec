Name:       liblc3plus
Version:    1.4.1
Release:    1%{?dist}
Summary:    Low Complexity Communication Codec Plus (LC3plus)
License:    Fraunhofer LC3plus Patent Licensing
URL:        https://www.iis.fraunhofer.de/en/ff/amm/communication/lc3.html

Source0:    https://github.com/arkq/LC3plus/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    https://www.iis.fraunhofer.de/content/dam/iis/en/img/ff/Audio/patent-lizenz/Fraunhofer-LC3plus-Licensing.pdf
Patch0:     https://github.com/arkq/LC3plus/commit/2942ea56482d993513b7fc3a8eea831f88dce2a6.patch
Patch1:     %{name}-build.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: perl

%description
LC3plus is LC3's sibling, equipped with numerous additional functionalities.
While comprising all features of LC3, including high speech and audio quality,
LC3plus incorporates functionalities for transmission robustness, extremely
low-delay use cases and high-resolution audio transmission. To improve
robustness, LC3plus contains a very high-performance packet loss concealment
algorithm as well as forward error correction schemes such as channel coding or
redundancy frame modes.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package utils
Summary: Utility package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Uitlities for command line use of and testing
the %{name} library.

%prep
%autosetup -p1 -n LC3plus-%{version}
cp %{SOURCE1} .

find . -name "*.c" -exec chmod 644 {} \;
find . -name "*.h" -exec chmod 644 {} \;

%build
cd src/floating_point
%make_build LC3plus
%make_build libLC3plus.so

%install
mkdir -p %{buildroot}%{_bindir} \
    %{buildroot}%{_includedir} \
    %{buildroot}%{_libdir}
install -p -m 0755 src/floating_point/LC3plus %{buildroot}%{_bindir}/
install -p -m 0755 src/floating_point/libLC3plus.so* %{buildroot}%{_libdir}/
install -p -m 0644 src/floating_point/lc3plus.h %{buildroot}%{_includedir}/

%check
cd testvec
./testvecCheck.pl -float

%files
%license Fraunhofer-LC3plus-Licensing.pdf
%{_libdir}/libLC3plus.so.*

%files devel
%{_includedir}/lc3plus.h
%{_libdir}/libLC3plus.so

%files utils
%{_bindir}/LC3plus

%changelog
* Mon Feb 05 2024 Simone Caronni <negativo17@gmail.com> - 1.4.1-1
- First build.
