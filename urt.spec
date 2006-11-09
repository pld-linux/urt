Summary:	Utah Raster Toolkit
Summary(pl):	Zestaw narzêdzi z Utah do grafiki rastrowej
Name:		urt
Version:	3.1b
Release:	5
License:	GPL-like/"reserved" (see documentation for details)
Group:		Applications/Graphics
Source0:	ftp://ftp.cs.utah.edu/pub/dept/OLD/pub/%{name}-%{version}.tar.Z
# Source0-md5:	c9a377284d00c102c1a8af53d95a6b39
Patch0:		%{name}-config.patch
Patch1:		%{name}-fixes.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-shared.patch
BuildRequires:	%{__perl}
BuildRequires:	XFree86-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	netpbm-devel >= 10
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

%description -l pl
Utah Raster Toolkit to zestaw programów i funkcji w C do obróbki
obrazów rastrowych czêsto wystêpuj±cych w grafice komputerowej. URT
dostarcza:
- Niezale¿ny od urz±dzenia i systemu format obrazków do zapisu grafiki
  i informacji o niej. Nazywa siê RLE i u¿ywa kompresji Run-Length
  Encoding, aby zmniejszyæ zajmowane miejsce.
- Zestaw funkcji w C do czytania, pisania i manipulowania obrazkami
  zapisanymi w formacie RLE.
- Zestaw programów do manipulowania i wy¶wietlania obrazków RLE.

%package devel
Summary:	Development files for Utah Raster Toolkit
Summary(pl):	Pakiet dla programistów Utah Raster Toolkit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Utah Raster Toolkit header files.

%description devel -l pl
Pliki nag³ówkowe Utah Raster Toolkit.

%package static
Summary:	Utah Raster Toolkit static library
Summary(pl):	Statyczna biblioteka Utah Raster Toolkit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	netpbm-rle-static
Obsoletes:	netpbm-rle-static
Conflicts:	netpbm-static < 9.23-2

%description static
Utah Raster Toolkit static library.

%description static -l pl
Statyczna biblioteka Utah Raster Toolkit.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
mv config/urt config/urt.old
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
	LIBX11="-L/usr/X11R6/%{_lib} -lX11" \
	LIBPBMPLUS="-lnetpbm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/rle} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3,5}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc 3.1-changes CHANGES README blurb copyright
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/rle
%{_mandir}/man[35]/*

%files static
%defattr(644,root,root,755)
%{_libdir}/librle.a
