Name:		adcli
Version:	0.8.0
Release:	1
Summary:	System/Configuration/Networking
License:	LGPLv2+
URL:		http://cgit.freedesktop.org/realmd/adcli
Source0:	http://www.freedesktop.org/software/realmd/releases/adcli-%{version}.tar.gz
BuildRequires:	intltool
BuildRequires:	gettext-devel
BuildRequires:	krb5-devel
BuildRequires:	openldap-devel
BuildRequires:	libxslt
BuildRequires:	xmlto
Requires:	sasl-plug-gssapi

%description
adcli is a tool for joining an Active Directory domain using
standard LDAP and Kerberos calls.

%prep
%setup -q

%build
%configure
%make

%check
make check

%install
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_datadir}/doc/adcli/*
%{_sbindir}/adcli
%{_mandir}/*/*
