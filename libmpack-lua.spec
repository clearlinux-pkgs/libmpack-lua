#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmpack-lua
Version  : 1.0.8
Release  : 2
URL      : https://github.com/libmpack/libmpack-lua/archive/1.0.8/libmpack-lua-1.0.8.tar.gz
Source0  : https://github.com/libmpack/libmpack-lua/archive/1.0.8/libmpack-lua-1.0.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: libmpack-lua-lib = %{version}-%{release}
Requires: libmpack-lua-license = %{version}-%{release}
BuildRequires : LuaJIT-dev
BuildRequires : libmpack-dev

%description
## libmpack lua binding
[![Travis Build Status](https://travis-ci.org/libmpack/libmpack-lua.svg?branch=master)](https://travis-ci.org/libmpack/libmpack-lua)

%package lib
Summary: lib components for the libmpack-lua package.
Group: Libraries
Requires: libmpack-lua-license = %{version}-%{release}

%description lib
lib components for the libmpack-lua package.


%package license
Summary: license components for the libmpack-lua package.
Group: Default

%description license
license components for the libmpack-lua package.


%prep
%setup -q -n libmpack-lua-1.0.8
cd %{_builddir}/libmpack-lua-1.0.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579207249
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}  USE_SYSTEM_LUA=yes USE_SYSTEM_MPACK=yes LUA_IMPL=luajit


%install
export SOURCE_DATE_EPOCH=1579207249
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmpack-lua
cp %{_builddir}/libmpack-lua-1.0.8/LICENSE-MIT %{buildroot}/usr/share/package-licenses/libmpack-lua/6a4d33353d2a8e515cb94ba0eac54ec4bfdabb50
%make_install USE_SYSTEM_LUA=yes USE_SYSTEM_MPACK=yes LUA_IMPL=luajit

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/lua/5.1/mpack.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmpack-lua/6a4d33353d2a8e515cb94ba0eac54ec4bfdabb50
