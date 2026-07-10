%global tl_name abnt
%global tl_revision 55471

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typesetting academic works according to ABNT rules
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/abnt
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abnt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abnt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The ABNT package provides a clean and practical implementation of the
ABNT rules for academic texts. Its purpose is to be as simple and user-
friendly as possible.

