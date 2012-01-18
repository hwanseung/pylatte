mod_pylatte.la: mod_pylatte.slo
	$(SH_LINK) -rpath $(libexecdir) -module -avoid-version  mod_pylatte.lo
DISTCLEAN_TARGETS = modules.mk
shared =  mod_pylatte.la
