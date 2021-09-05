.. _EDAA:Context:

Context
#######

`IP Core Management Infrastructure (pyIPCMI) <https://github.com/Paebbels/pyIPCMI>`__, which was originally part of the
`Pile of Cores (PoC) <https://github.com/VLSI-EDA/PoC>`__ library, is a set of Python modules stacked on top of each other.
The core parts of pyIPCMI abstract the interaction with CLI tools and EDA tools (for simulation, synthesis, IP core
extraction/generation/packaging, ), as well as finding executables in multi-installation setups, post-processing of
outputs, etc.
However, similarly to other HDL/EDA management tools, pyIPCMI was conceived as a monolith.
That is, abstraction layers were written as a result of applying good coding and application development practices; not
necessarily with third-parties reusing them in mind.

Unfortunately, when pyIPCMI was developed INI files were used as the main user provided configuration file format, due
to usage of JSON and YAML not being widespread back then.
That didn't age well, as the INI format is rarely used in open source EDA projects.
Fortunately, the main developer of pyIPCMI is willing to rework the codebase, update it, and split the abstraction
layers explicitly to match the :ref:`EDAA:Model`.
Those modules are being reworked under the umbrella of EDA².

*TBC*

* *cocotb*
* *OSVVM*
* *VUnit*
* *FuseSoC/Edalize/fsva*
