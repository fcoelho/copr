%global srcname jqp

Name: jqp
Version: 0.1.1
Release: 1%{?dist}
License: MIT
Summary: a TUI playground for exploring jq.
Url: https://github.com/noahgorstein/jqp
# Sources can be obtained by
# git clone https://pagure.io/copr-tito-quickdoc
# cd copr-tito-quickdoc
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

%description
a TUI playground for exploring jq.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build

%install

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{_bindir}/hellocopr
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Thu Sep 22 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 0.1.1-1
- new package built with tito

