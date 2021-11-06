logo-run:
	docker run --rm -v /$(PWD)://wrk -w //wrk ghcr.io/edaa-org/edaa/svg sh -c 'xvfb-run ./_logo/generate_project_banners.sh'

logo-build:
	docker build -t ghcr.io/edaa-org/edaa/svg - < .github/edaa--svg.dockerfile

#---

SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees -T -D language=en $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

#---

man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man

#---

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html

#---

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
