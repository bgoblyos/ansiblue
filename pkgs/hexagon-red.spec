Name:           hexagon-red
Version:        0.0.1
Release:        2
Summary:        Hexagon RED plymouth theme
BuildArch:      noarch

License:        GPL3
Source0:        %{name}-%{version}.tar.gz

Requires:       plymouth, plymouth-plugin-script

%description
Hexagon RED plymouth theme

%prep
%autosetup


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/plymouth/themes/
cp -r hexagon_red $RPM_BUILD_ROOT/usr/share/plymouth/themes/

%files
/usr/share/plymouth/themes/hexagon_red



%changelog
* Thu Apr 13 2023 Bence
- 
