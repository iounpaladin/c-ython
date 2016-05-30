python_version_full := $(wordlist 2,4,$(subst ., ,$(shell python -V --version 2>&1)))
python_version_major := $(word 1,${python_version_full})
python_version_minor := $(word 2,${python_version_full})
python_version_patch := $(word 3,${python_version_full})

install : *
	cp -Rf cppython /usr/lib/python${python_version_major}.${python_version_minor}/site-packages/

