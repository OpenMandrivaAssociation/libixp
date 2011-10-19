%define develname %mklibname ixp -d

%define	changeset	339db5c6d2c9
# no version tagged, just in the NEWS file
%define hgdate		20110223

Name: libixp
Version: 0.6
Release: %mkrel -c %{hgdate} 2
Summary: Plan9 file protocol library
License: MIT
Group: System/Libraries
URL: http://www.suckless.org/wiki/libs/libixp
Source: http://hg.suckless.org/libixp/archive/%{changeset}.tar.gz

%description
libixp is a stand-alone client/server 9P library.
libixp's server api is heavily based on that of Plan 9's lib9p.

%prep
%setup -qn %{name}-%{changeset}

%build
sed -i \
    -e "/^PREFIX/s|=.*|= /usr|" \
%ifarch x86_64
	-e "s|/usr/lib|/usr/lib64|g" \
	-e "/ LIBDIR/s|=.*|= /usr/lib64|" \
%endif
	config.mk

%make

%install
%makeinstall_std

%package -n %{develname}
Summary: Plan9 file protocol library
Group: Development/C
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
libixp is a stand-alone client/server 9P library.
libixp's server api is based heavily on that of Plan 9's lib9p.

%files -n %{develname}
%{_libdir}/*.a
%{_includedir}/ixp.h
%{_includedir}/ixp_srvutil.h
%{_mandir}/man3/*.3*

%package -n ixpc
Summary: Plan9 file protocol client
Group: Networking/File transfer

%description -n ixpc
ixpc is a client to access a 9P file server from the command line
or from shell scripts.

%files -n ixpc
%{_bindir}/ixpc
%{_mandir}/man1/ixpc.1*
