Name: jqp
Version: 0.1.0
Release: 1%{?dist}
License: MIT
Summary: a TUI playground for exploring jq.
URL: https://github.com/noahgorstein/jqp

%description
a TUI playground for exploring jq.

%prep
# installing a binary, no source code used

%build
# cd %{_builddir}
curl -LO https://github.com/noahgorstein/jqp/releases/download/v%{version}/jqp_%{version}_Linux_%{_arch}.tar.gz
tar xf jqp_%{version}_Linux_%{_arch}.tar.gz

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/licenses/jqp/
mkdir -p %{buildroot}/usr/share/doc/jqp/

install -m 755 jqp %{buildroot}/usr/bin/jqp
install -m 644 LICENSE %{buildroot}/usr/share/licenses/jqp/LICENSE
install -m 644 README.md %{buildroot}/usr/share/doc/jqp/README.md

#-- FILES ---------------------------------------------------------------------#
%files
/usr/bin/jqp
/usr/share/licenses/jqp/LICENSE
/usr/share/doc/jqp/README.md

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Thu Sep 22 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 0.1.0-1
- release 0.1.0
