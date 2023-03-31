Name:		texlive-xetex-pstricks
Version:	17055
Release:	2
Summary:	Running PStricks under XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/xetex/pstricks
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-pstricks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-pstricks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an indirection scheme for XeTeX to use the
pstricks xdvipdfmx.cfg configuration file, so that XeTeX
documents will load it in preference to the standard
pstricks.con configuration file. With this configuration, many
PSTricks features can be used in xelatex or plain xetex
documents.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xetex-pstricks/pstricks.con
%{_texmfdistdir}/tex/xetex/xetex-pstricks/pstricks.con
%doc %{_texmfdistdir}/doc/xetex/xetex-pstricks/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
