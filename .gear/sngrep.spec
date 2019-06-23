Name: sngrep
Version: 1.4.2
Release: alt3

Summary: sngrep is a tool for displaying SIP calls message flows from terminal

License: GPLv2+
Group: Networking/Other
Url: https://github.com/irontec/sngrep

Source: %name-%version.tar

Patch0: %name-%version-alt.patch

BuildRequires: libncurses-devel libpcap libgnutls-devel libpcap-devel libpcre-devel libgcrypt-devel


%description
sngrep is a tool for displaying SIP calls message flows from terminal.
It supports live capture to display realtime SIP packets and can also be used
as PCAP viewer.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure \
	   --enable-eep \
	   --with-gnutls \
	   --with-pcre \
#

%make_build

%install
%makeinstall_std

%files
%_sysconfdir/sngreprc
%_bindir/sngrep
%_man8dir/sngrep.8*

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt2
- NMU: remove %ubt from release

* Wed Apr 12 2017 Evgeny Bolshedvorsky <jenya@altlinux.org> 1.4.2-alt1%ubt
- added ubt

* Mon Apr 10 2017 Evgeny Bolshedvorsky <jenya@altlinux.org> 1.4.2-alt1
- initial build
