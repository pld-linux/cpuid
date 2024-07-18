Summary:	x86 CPUID information display program
Summary(pl.UTF-8):	Program wyświetlający informacje CPUID dla procesorów x86
Name:		cpuid
Version:	20240716
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://www.etallen.com/cpuid/%{name}-%{version}.src.tar.gz
# Source0-md5:	36f9e43e3273f32444f3d7c080efa10a
URL:		https://www.etallen.com/cpuid.html
ExclusiveArch:	%{ix86} %{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program that displays detailed information about x86 CPU(s) gathered
from the CPUID instruction.

%description -l pl.UTF-8
Program wyświetlający szczegółowe informacje na temat zainstalowanego
procesora (lub procesorów) x86 zebrane przy użyciu instrukcji CPUID.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_sbindir}
cp -a %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog FAMILY.NOTES FUTURE
%attr(755,root,root) %{_sbindir}/cpuid
%{_mandir}/man1/cpuid.1*
