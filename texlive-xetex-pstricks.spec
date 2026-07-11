%global tl_name xetex-pstricks
%global tl_revision 17055

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Running PSTricks under XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/xetex/pstricks
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-pstricks.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetex-pstricks.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an indirection scheme for XeTeX to use the pstricks
xdvipdfmx.cfg configuration file, so that XeTeX documents will load it
in preference to the standard pstricks.con configuration file. With this
configuration, many PSTricks features can be used in XeLaTeX or plain
XeTeX documents.

