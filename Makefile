PREFIX = /usr
SYSCFG = /etc

sbindir = $(PREFIX)/sbin
servicedir = $(PREFIX)/lib/obs/service

all:

install:
	install -d $(DESTDIR)$(servicedir)
	install -m 0755 bazel_repositories $(DESTDIR)$(servicedir)
	install -m 0644 bazel_repositories.service $(DESTDIR)$(servicedir)

test:
	flake8 bazel_repositories
