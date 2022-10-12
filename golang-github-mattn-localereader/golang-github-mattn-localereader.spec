# https://github.com/charmbracelet/bubbletea
%global goipath         github.com/mattn/go-localereader
Version: 2
%global commit 2491eb6c1c75720122ef321ed7acc3a8d9de95b1

%gometa

%global common_description %{expand:
CodePage decoder for Windows}

%global golicenses    LICENSE

Name:           %{goname}
Release:        1%{?dist}
Summary:        CodePage decoder for Windows
License:        MIT
URL:            %{gourl}
Source:         %{gosource}

# BuildRequires: golang(github.com/containerd/console)
# BuildRequires: golang(github.com/mattn/go-isatty)
# BuildRequires: golang(github.com/mattn/go-localereader)
# BuildRequires: golang(github.com/pmezard/go-difflib/difflib)
# BuildRequires: golang(github.com/stretchr/objx)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%check
%gocheck

%gopkgfiles


%changelog
* Wed Oct 12 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 2-1
- 

* Wed Oct 12 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com> 1-1
- new package built with tito

* Mon Oct 03 2022 Felipe Bessa Coelho <felipe.coelho@deskpro.com>
- osiosdifosd (felipe.coelho@deskpro.com)
- aosdasduoi (felipe.coelho@deskpro.com)
- oaoidasdioasiod (felipe.coelho@deskpro.com)


