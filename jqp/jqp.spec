%global srcname jqp
%define _disable_source_fetch 0

Name: jqp
Version: 0.1.0
Release: 1%{?dist}
License: MIT
Summary: a TUI playground for exploring jq.
Url: https://github.com/noahgorstein/jqp
# Sources can be obtained by
# git clone https://pagure.io/copr-tito-quickdoc
# cd copr-tito-quickdoc
# tito build --tgz
Source0: https://github.com/noahgorstein/jqp/releases/download/v%{version}/jqp_%{version}_Linux_%{_arch}.tar.gz

%description
a TUI playground for exploring jq.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup -v
# curl -LO https://github.com/noahgorstein/jqp/releases/download/v%{version}/jqp_%{version}_Linux_%{_arch}.tar.gz

tar xf jqp_%{version}_Linux_%{_arch}.tar.gz

%build

%install
cp -rfa * %{buildroot}

#-- FILES ---------------------------------------------------------------------#
%files

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Thu Sep 22 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 0.1.0-1
- release 0.1.0
