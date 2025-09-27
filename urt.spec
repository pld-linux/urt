Summary:	Utah Raster Toolkit
Summary(pl.UTF-8):	Zestaw narzędzi z Utah do grafiki rastrowej
Name:		urt
Version:	3.1b
Release:	10
License:	GPL-like/"reserved" (see documentation for details)
Group:		Applications/Graphics
# dead server, now available at https://github.com/sarnold/urt
Source0:	ftp://ftp.iastate.edu/pub/utah-raster/%{name}-%{version}.tar.Z
# Source0-md5:	c9a377284d00c102c1a8af53d95a6b39
Patch0:		%{name}-config.patch
Patch1:		%{name}-fixes.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-shared.patch
URL:		https://www2.cs.utah.edu/gdc/projects/urt/
BuildRequires:	%{__perl}
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	netpbm-devel >= 10
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Utah Raster toolkit is a collection of programs and C routines for
dealing with raster images commonly encountered in computer graphics.
It provides the following major functions:
- A device and system independent image format for storing images and
  information about them. Called the RLE format, it uses run length
  encoding to reduce storage space for most images.
- A library of C routines for reading, writing and manipulating images
  stored in the RLE format.
- A collections of programs for manipulating and displaying RLE
  images.

%description -l pl.UTF-8
Utah Raster Toolkit to zestaw programów i funkcji w C do obróbki
obrazów rastrowych często występujących w grafice komputerowej. URT
dostarcza:
- Niezależny od urządzenia i systemu format obrazków do zapisu grafiki
  i informacji o niej. Nazywa się RLE i używa kompresji Run-Length
  Encoding, aby zmniejszyć zajmowane miejsce.
- Zestaw funkcji w C do czytania, pisania i manipulowania obrazkami
  zapisanymi w formacie RLE.
- Zestaw programów do manipulowania i wyświetlania obrazków RLE.

%package libs
Summary:	Utah Raster Toolkit shared library
Summary(pl.UTF-8):	Biblioteka współdzielona Utah Raster Toolkit
Group:		Libraries
Conflicts:	urt < 3.1b-9

%description libs
Utah Raster Toolkit shared library.

%description libs -l pl.UTF-8
Biblioteka współdzielona Utah Raster Toolkit.

%package devel
Summary:	Development files for Utah Raster Toolkit
Summary(pl.UTF-8):	Pakiet dla programistów Utah Raster Toolkit
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Utah Raster Toolkit header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe Utah Raster Toolkit.

%package static
Summary:	Utah Raster Toolkit static library
Summary(pl.UTF-8):	Statyczna biblioteka Utah Raster Toolkit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	netpbm-rle-static
Obsoletes:	netpbm-rle-static
Conflicts:	netpbm-static < 9.23-2

%description static
Utah Raster Toolkit static library.

%description static -l pl.UTF-8
Statyczna biblioteka Utah Raster Toolkit.

%prep
%setup -q -c
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%{__mv} config/urt config/urt.old
sed -e's,^##defpath MAN_DEST.*,#defpath MAN_DEST %{_mandir},' \
	-e's,^##defpath LIB_DEST.*,#defpath LIB_DEST %{_libdir},' \
	-e's,^##defpath GET_DEST.*,#defpath GET_DEST %{_bindir},' \
	-e's,^##defpath CNV_DEST.*,#defpath CNV_DEST %{_bindir},' \
	-e's,^##defpath TOOLS_DEST.*,#defpath TOOLS_DEST %{_bindir},' \
	-e's,^##defpath INC_DEST.*,#defpath INC_DEST %{_includedir}/rle,' \
	config/urt.old > config/urt

./Configure
%{__make} \
	CC="%{__cc}" \
	ExtraCFLAGS="%{rpmcflags}" \
	LIBPBMPLUS="-lnetpbm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/rle} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3,5}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aliastorle
%attr(755,root,root) %{_bindir}/applymap
%attr(755,root,root) %{_bindir}/avg4
%attr(755,root,root) %{_bindir}/crop
%attr(755,root,root) %{_bindir}/cubitorle
%attr(755,root,root) %{_bindir}/fant
%attr(755,root,root) %{_bindir}/geticr
%attr(755,root,root) %{_bindir}/getx11
%attr(755,root,root) %{_bindir}/giftorle
%attr(755,root,root) %{_bindir}/graytorle
%attr(755,root,root) %{_bindir}/into
%attr(755,root,root) %{_bindir}/mcut
%attr(755,root,root) %{_bindir}/mergechan
%attr(755,root,root) %{_bindir}/painttorle
%attr(755,root,root) %{_bindir}/pgmtorle
%attr(755,root,root) %{_bindir}/ppmtorle
%attr(755,root,root) %{_bindir}/pyrmask
%attr(755,root,root) %{_bindir}/rawtorle
%attr(755,root,root) %{_bindir}/repos
%attr(755,root,root) %{_bindir}/rlatorle
%attr(755,root,root) %{_bindir}/rleClock
%attr(755,root,root) %{_bindir}/rleaddcom
%attr(755,root,root) %{_bindir}/rlebg
%attr(755,root,root) %{_bindir}/rlebox
%attr(755,root,root) %{_bindir}/rlecat
%attr(755,root,root) %{_bindir}/rleccube
%attr(755,root,root) %{_bindir}/rlecomp
%attr(755,root,root) %{_bindir}/rledither
%attr(755,root,root) %{_bindir}/rleflip
%attr(755,root,root) %{_bindir}/rlegrid
%attr(755,root,root) %{_bindir}/rlehdr
%attr(755,root,root) %{_bindir}/rlehisto
%attr(755,root,root) %{_bindir}/rleldmap
%attr(755,root,root) %{_bindir}/rlemandl
%attr(755,root,root) %{_bindir}/rlenoise
%attr(755,root,root) %{_bindir}/rlepatch
%attr(755,root,root) %{_bindir}/rleprint
%attr(755,root,root) %{_bindir}/rlequant
%attr(755,root,root) %{_bindir}/rlescale
%attr(755,root,root) %{_bindir}/rleselect
%attr(755,root,root) %{_bindir}/rlesetbg
%attr(755,root,root) %{_bindir}/rlespiff
%attr(755,root,root) %{_bindir}/rlesplice
%attr(755,root,root) %{_bindir}/rlesplit
%attr(755,root,root) %{_bindir}/rlestereo
%attr(755,root,root) %{_bindir}/rleswap
%attr(755,root,root) %{_bindir}/rletoabA60
%attr(755,root,root) %{_bindir}/rletoabA62
%attr(755,root,root) %{_bindir}/rletoalias
%attr(755,root,root) %{_bindir}/rletoascii
%attr(755,root,root) %{_bindir}/rletogif
%attr(755,root,root) %{_bindir}/rletogray
%attr(755,root,root) %{_bindir}/rletopaint
%attr(755,root,root) %{_bindir}/rletoppm
%attr(755,root,root) %{_bindir}/rletops
%attr(755,root,root) %{_bindir}/rletoraw
%attr(755,root,root) %{_bindir}/rletorla
%attr(755,root,root) %{_bindir}/rletotarga
%attr(755,root,root) %{_bindir}/rletotiff
%attr(755,root,root) %{_bindir}/rlezoom
%attr(755,root,root) %{_bindir}/smush
%attr(755,root,root) %{_bindir}/targatorle
%attr(755,root,root) %{_bindir}/tifftorle
%attr(755,root,root) %{_bindir}/to8
%attr(755,root,root) %{_bindir}/tobw
%attr(755,root,root) %{_bindir}/unexp
%attr(755,root,root) %{_bindir}/unslice
%attr(755,root,root) %{_bindir}/wasatchrle
%attr(755,root,root) %{_bindir}/xbmtorle
%{_mandir}/man1/aliastorle.1*
%{_mandir}/man1/applymap.1*
%{_mandir}/man1/avg4.1*
%{_mandir}/man1/crop.1*
%{_mandir}/man1/cubitorle.1*
%{_mandir}/man1/dvirle.1*
%{_mandir}/man1/fant.1*
%{_mandir}/man1/get4d.1*
%{_mandir}/man1/get_orion.1*
%{_mandir}/man1/getami.1*
%{_mandir}/man1/getap.1*
%{_mandir}/man1/getbob.1*
%{_mandir}/man1/getcx3d.1*
%{_mandir}/man1/getfb.1*
%{_mandir}/man1/getgmr.1*
%{_mandir}/man1/getiris.1*
%{_mandir}/man1/getmex.1*
%{_mandir}/man1/getqcr.1*
%{_mandir}/man1/getren.1*
%{_mandir}/man1/getsun.1*
%{_mandir}/man1/gettaac.1*
%{_mandir}/man1/getx10.1*
%{_mandir}/man1/getx11.1*
%{_mandir}/man1/giftorle.1*
%{_mandir}/man1/graytorle.1*
%{_mandir}/man1/into.1*
%{_mandir}/man1/mcut.1*
%{_mandir}/man1/mergechan.1*
%{_mandir}/man1/painttorle.1*
%{_mandir}/man1/pgmtorle.1*
%{_mandir}/man1/ppmtorle.1*
%{_mandir}/man1/pyrmask.1*
%{_mandir}/man1/rastorle.1*
%{_mandir}/man1/rawtorle.1*
%{_mandir}/man1/read98721.1*
%{_mandir}/man1/repos.1*
%{_mandir}/man1/rlatorle.1*
%{_mandir}/man1/rleClock.1*
%{_mandir}/man1/rleaddcom.1*
%{_mandir}/man1/rleaddeof.1*
%{_mandir}/man1/rlebg.1*
%{_mandir}/man1/rlebox.1*
%{_mandir}/man1/rlecat.1*
%{_mandir}/man1/rleccube.1*
%{_mandir}/man1/rlecomp.1*
%{_mandir}/man1/rledither.1*
%{_mandir}/man1/rleflip.1*
%{_mandir}/man1/rlegrid.1*
%{_mandir}/man1/rlehdr.1*
%{_mandir}/man1/rlehisto.1*
%{_mandir}/man1/rleinterp.1*
%{_mandir}/man1/rleldmap.1*
%{_mandir}/man1/rlemandl.1*
%{_mandir}/man1/rlenoise.1*
%{_mandir}/man1/rlepatch.1*
%{_mandir}/man1/rleprint.1*
%{_mandir}/man1/rlequant.1*
%{_mandir}/man1/rlescale.1*
%{_mandir}/man1/rleselect.1*
%{_mandir}/man1/rlesetbg.1*
%{_mandir}/man1/rlespiff.1*
%{_mandir}/man1/rlesplice.1*
%{_mandir}/man1/rlesplit.1*
%{_mandir}/man1/rlestereo.1*
%{_mandir}/man1/rleswap.1*
%{_mandir}/man1/rletoabA60.1*
%{_mandir}/man1/rletoabA62.1*
%{_mandir}/man1/rletoalias.1*
%{_mandir}/man1/rletoascii.1*
%{_mandir}/man1/rletocgm.1*
%{_mandir}/man1/rletogif.1*
%{_mandir}/man1/rletogray.1*
%{_mandir}/man1/rletopaint.1*
%{_mandir}/man1/rletoppm.1*
%{_mandir}/man1/rletops.1*
%{_mandir}/man1/rletorast.1*
%{_mandir}/man1/rletoraw.1*
%{_mandir}/man1/rletorla.1*
%{_mandir}/man1/rletotarga.1*
%{_mandir}/man1/rletotiff.1*
%{_mandir}/man1/rlezoom.1*
%{_mandir}/man1/show3.1*
%{_mandir}/man1/smush.1*
%{_mandir}/man1/targatorle.1*
%{_mandir}/man1/tifftorle.1*
%{_mandir}/man1/to8.1*
%{_mandir}/man1/tobw.1*
%{_mandir}/man1/unexp.1*
%{_mandir}/man1/unslice.1*
%{_mandir}/man1/urt.1*
%{_mandir}/man1/wasatchrle.1*

%files libs
%defattr(644,root,root,755)
%doc 3.1-changes CHANGES README blurb copyright
%attr(755,root,root) %{_libdir}/librle.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librle.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librle.so
%{_libdir}/librle.la
%{_includedir}/rle
%{_mandir}/man3/buildmap.3*
%{_mandir}/man3/bwdithermap.3*
%{_mandir}/man3/colorquant.3*
%{_mandir}/man3/dither*.3*
%{_mandir}/man3/float_to_exp.3*
%{_mandir}/man3/hilbert*.3*
%{_mandir}/man3/inv_cmap.3*
%{_mandir}/man3/librle.3*
%{_mandir}/man3/make_square.3*
%{_mandir}/man3/rgb_to_bw.3*
%{_mandir}/man3/rle_*.3*
%{_mandir}/man5/RLE.5*
%{_mandir}/man5/rle.5*

%files static
%defattr(644,root,root,755)
%{_libdir}/librle.a
