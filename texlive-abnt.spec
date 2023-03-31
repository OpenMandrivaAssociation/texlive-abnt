Name:		texlive-abnt
Version:	55471
Release:	2
Summary:	Typesetting academic works according to ABNT rules
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/abnt
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abnt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abnt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The ABNT package provides a clean and practical implementation
of the ABNT rules for academic texts. Its purpose is to be as
simple and user-friendly as possible.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/abnt
%doc %{_texmfdistdir}/doc/latex/abnt

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
