%global goipath         gopkg.in/noahgorstein/jqp.v0
%global forgeurl        https://github.com/noahgorstein/jqp
Version:                0.1.0

%gometa

%global common_description %{expand:
a TUI playground for exploring jq.}

%global golicenses    LICENSE
%global godocs        *.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        a TUI playground for exploring jq.
License:        MIT
URL:            %{gourl}
Source:         %{gosource}

# BuildRequires: golang(golang.org/x/crypto/ed25519)
# BuildRequires: golang(golang.org/x/crypto/pbkdf2)
# BuildRequires: golang(github.com/stretchr/testify/assert)
# BuildRequires: golang(gopkg.in/alecthomas/kingpin.v2)

# BuildRequires: golang(github.com/alecthomas/chroma)
# BuildRequires: golang(github.com/atotto/clipboard)
# BuildRequires: golang(github.com/charmbracelet/bubbles)
# BuildRequires: golang(github.com/charmbracelet/bubbletea)
# BuildRequires: golang(github.com/charmbracelet/lipgloss)
# BuildRequires: golang(github.com/itchyny/gojq)
# BuildRequires: golang(github.com/muesli/termenv)
# BuildRequires: golang(github.com/spf13/cobra)
# BuildRequires: golang(github.com/spf13/pflag)
# BuildRequires: golang(github.com/spf13/viper)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%gocheck

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Thu Sep 22 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 0.1.0-1
- release 0.1.0
