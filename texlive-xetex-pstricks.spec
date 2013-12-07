# revision 17055
# category Package
# catalog-ctan /graphics/xetex/pstricks
# catalog-date 2010-02-18 14:04:58 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-xetex-pstricks
Version:	20100218
Release:	5
Summary:	Running PStricks under XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/xetex/pstricks
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-pstricks.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-pstricks.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100218-2
+ Revision: 757644
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100218-1
+ Revision: 719934
- texlive-xetex-pstricks
- texlive-xetex-pstricks
- texlive-xetex-pstricks

