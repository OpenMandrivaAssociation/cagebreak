Name:		cagebreak
Version:	3.2.1
Release:        1
Summary:	A tiling Wayland compositor
Group:		Window Manager
License:	MIT
URL:		https://github.com/project-repo/cagebreak
Source0:	https://github.com/project-repo/cagebreak/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(wlroots-0.20)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(scdoc)

BuildSystem:	meson
BuildOption:	-Dxwayland=true
BuildOption:	-Dman-pages=true
BuildOption:	--buildtype=release

%description
%{summary} based on cage.
It breaks the kiosk aspect of cage into tiles, hence the name.

%files
%license LICENSE
%{_sysconfdir}/xdg/%{name}/config
%{_bindir}/%{name}
%{_mandir}/*/%{name}*
