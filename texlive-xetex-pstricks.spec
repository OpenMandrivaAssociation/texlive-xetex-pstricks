# revision 17055
# category Package
# catalog-ctan /graphics/xetex/pstricks
# catalog-date 2010-02-18 14:04:58 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-xetex-pstricks
Version:	20100218
Release:	1
Summary:	Running PStricks under XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/xetex/pstricks
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-pstricks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-pstricks.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The package provides an indirection scheme for XeTeX to use the
pstricks xdvipdfmx.cfg configuration file, so that XeTeX
documents will load it in preference to the standard
pstricks.con configuration file. With this configuration, many
PSTricks features can be used in xelatex or plain xetex
documents.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/xetex-pstricks/pstricks.con
%{_texmfdistdir}/tex/xetex/xetex-pstricks/pstricks.con
%doc %{_texmfdistdir}/doc/xetex/xetex-pstricks/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
