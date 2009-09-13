%define major 0
%define libname %mklibname ixp %{major}
%define develname %mklibname ixp -d

Name: libixp
Version: 0.5
Release: %mkrel 2
Summary: Plan9 file protocol library
License: MIT
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.suckless.org/wiki/libs/libixp
Source: %name-%version.tar.gz

%description
libixp is a stand-alone client/server 9P library.
libixp's server api is heavily based on that of Plan 9's lib9p.

%prep
%setup -q -n %name-%version

%build
%make PREFIX=/usr ETC=/etc

%install
%make install PREFIX=%{buildroot}/usr ETC=%{buildroot}/etc

%files
%doc libixp/LICENSE*

%package -n %{develname}
Summary: Plan9 file protocol library
Group: Development/C
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
libixp is a stand-alone client/server 9P library.
libixp's server api is based heavily on that of Plan 9's lib9p.

%files -n %{develname}
/usr/lib/*.a
%{_includedir}/ixp.h
%{_includedir}/ixp_srvutil.h

%package -n ixpc
Summary: Plan9 file protocol client
Group: Networking/File transfer
Requires: %name = %version-%release

%description -n ixpc
ixpc is a client to access a 9P file server from the command line
or from shell scripts.

%files -n ixpc
%{_bindir}/ixpc
%{_mandir}/man1/ixpc.1*
