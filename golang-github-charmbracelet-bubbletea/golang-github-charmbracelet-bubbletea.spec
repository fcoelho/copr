# https://github.com/charmbracelet/bubbletea
%global goipath         github.com/charmbracelet/bubbletea
Version:                0.22.1

%gometa

%global common_description %{expand:
A Go framework based on The Elm Architecture. Bubble Tea is well-suited for
simple and complex terminal applications, either inline, full-window, or a mix
of both.}

%global golicenses    LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        The fun, functional and stateful way to build terminal apps
License:        MIT
URL:            %{gourl}
Source:         %{gosource}

BuildRequires: golang(github.com/containerd/console)
BuildRequires: golang(github.com/mattn/go-isatty)
BuildRequires: golang(github.com/mattn/go-localereader)
# BuildRequires: golang(github.com/pmezard/go-difflib/difflib)
# BuildRequires: golang(github.com/stretchr/objx)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%gopkgfiles

%changelog
* Wed Oct 12 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 0.22.1-2
- 

