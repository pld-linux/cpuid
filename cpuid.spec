Summary:	x86 CPUID display program
Summary(pl):	CPUID dla procesorów x86
Name:		cpuid
Version:	3.3
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www.ka9q.net/code/cpuid/%{name}-%{version}.tar.gz
# Source0-md5:	641af7bb12e1feb0b0d97ed68908297c
URL:		http://www.ka9q.net/code/cpuid/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program that displays details about x86 installed processor.

%description -l pl
Program wy¶wietlaj±cy szczegó³owe informacje na temat zainstalowanego
procesora (x86).

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install cpuid $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
