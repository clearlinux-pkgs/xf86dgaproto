#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86dgaproto
Version  : 2.1
Release  : 11
URL      : http://xorg.freedesktop.org/archive/individual/proto/xf86dgaproto-2.1.tar.bz2
Source0  : http://xorg.freedesktop.org/archive/individual/proto/xf86dgaproto-2.1.tar.bz2
Summary  : XF86DGA extension headers
Group    : Development/Tools
License  : MIT-feh

%description
No detailed description available

%package dev
Summary: dev components for the xf86dgaproto package.
Group: Development
Provides: xf86dgaproto-devel

%description dev
dev components for the xf86dgaproto package.


%prep
%setup -q -n xf86dgaproto-2.1

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/xf86dga.h
/usr/include/X11/extensions/xf86dga1const.h
/usr/include/X11/extensions/xf86dga1proto.h
/usr/include/X11/extensions/xf86dga1str.h
/usr/include/X11/extensions/xf86dgaconst.h
/usr/include/X11/extensions/xf86dgaproto.h
/usr/include/X11/extensions/xf86dgastr.h
/usr/lib64/pkgconfig/xf86dgaproto.pc
