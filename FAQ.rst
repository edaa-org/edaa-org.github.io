.. _FAQ:

Frequently Asked Questions (FAQ)
################################


.. _FAQ:What:

What problem(s) is EDA² going to solve?
=======================================

Reduce code duplication in open source EDA tooling frameworks, which takes significant effort as a community (both users
and maintainers) and does not add value *per se*, since most of them support the same tools.
In the last decade more than a dozen frameworks were prototyped in Python, EDA² is a proposal to gather the common and
reusable components of the frameworks preserving the unique workflows and user experience of each of them.
See a list of some of these frameworks in :ref:`EDAA:Workflows`.

Context
-------

Most of the Python frameworks to ease the usage of EDA tools were written with a desired user experience (UX) in mind.
The typical supported workflows (use cases) are running simulations with traditional vendor tools and with open source
tools, or running both simulation and synthesis with the same sets of HDL sources.
That is, the design of the frameworks started from a homogeneous API (either a Python class, a CLI, and/or a configuration
file format and syntax) to reduce the complexity of dealing with multiple EDA tools.
Moreover, most of them were born as in-house scripts and utilities before evolving into open source packages.
As a result, the organisation and structure of the internals were not explicitly defined in many of those projects.
There is a non-negligible amount of almost exact code duplication in the community, because all of them need to deal
with the definition of filesets, interacting with tool CLIs, processing logs/results, etc. of the same EDA tools.
However, we find they all have incompatible codebases because they are based on the configuration object retrieved from
user input; and each framework uses a diferent object format.

Project declarations
--------------------

Having incompatible project objects produces fragmentation in the user bases, because it increases the burden to try
other tools after one configuration approach is adopted.
Therefore, the main problem EDA² is trying to solve is interoperability of project definitions.
Users should be able to declare their sources once only, using a purely declarative style and/or imperatively through a
full-blown language.

Unfortunately, writing dozens of 1-to-1 conversion utilities to translate from each one framework to another would
significantly increase maintainence of the ecosystem and it's not affordable.
Hence, the project formats of existing solutions were analysed and a Python API was defined:
:doc:`pyEDAA.ProjectModel ➚ <projectmodel:index>`.
See also
:doc:`pyVHDLModel ➚ <vhdlmodel:index>`,
:doc:`pySVModel ➚ <svmodel:index>`
and :doc:`pyEDAA.IPXACT ➚ <ipxact:index>`.
EDA²'s ProjectModel is designed to support a superset of the (meta)data that existing Python frameworks need.
Hence, writing at most one conversion utility for each framework will allow users to reuse project declarations.

.. NOTE::
  An obvious question in this context is: `xkcd.com/927: How standards proliferate <https://xkcd.com/927/>`__.

  * It was discussed with the maintainers of several of the existing frameworks how to provide a documented and
    entrypoint-agnostic Python API; one that supports both simulation and synthesis with either traditional vendor or
    open source tools.
    However, for sensible reasons, some of the desired features did not fall into their immediate scope.
  * EDA²'s ProjectModel is actually based on `Paebbels/pyIPCMI: pyIPCMI/Base/Project.py <https://github.com/Paebbels/pyIPCMI/blob/master/pyIPCMI/Base/Project.py>`__.
    It was split and enhanced to make it agnostic to the internals of pyIPCMI.

Configuration files
-------------------

Several discussions in the community lead to the conclusion that purely declarative configuration files cannot support
intermediate and complex workflows.
Most of the projects had some declarative syntax, but were then extended to effectively implement some Domain Specific
Language (DSL) allowing imperative definition of sources and targets.
In order to avoid the maintenance burden of dealing with multiple DSLs at first, :doc:`pyEDAA.ProjectModel ➚ <projectmodel:index>`
is defined as a Python API.
Since the frameworks use Python, a Python API allows either:

* A purely declarative style, as in pyFPGA.
* An imperative style (optionally using any Python module), as in VUnit.
* Reusing existing modules for reading ``.ini``, ``.yml``, ``.json``, ``.core``, ``.pro``, ... files, as in FuseSoC,
  Edalize, pyIPCMI or OSVVM.

EDA tool wrappers
-----------------

Apart from gathering user input (through files or CLI), all the frameworks need to interact with CLIs of EDA tools.
In fact, the main difference between frameworks is how they select and organise the sources declared in the project, in
order to run each EDA tool and get results.
Therefore, features to compose CLI arguments, to handle ``stdin``, ``stdout`` and ``stderr`` to redirect logs, pipe
commands and/or use the shell interpreter are duplicated in all the framework.
Again, most implementations receive mainly an object with the same format as the project, which makes the implementations
incompatible despite being almost the same.

:doc:`pyEDAA.CLITool ➚ <clitool:index>` provides Python APIs agnostic to any specific project model/format.
Similarly to `docker-py.rtfd.io ➚ <https://docker-py.readthedocs.io>`__, each EDA tool is wrapped in an independent class
mapped to the CLI interface.
CLITool allows frameworks to focus on the content in Python, instead of dealing with translating the parameters to CLI
arguments and handling the environment of the call.

.. NOTE::
  EDA²'s CLITool is based on :doc:`pyTooling.CLIAbstraction ➚ <cliabstraction:index>`, a toolkit for wrapping CLI tools
  in Python.

.. HINT::
  CLITool is extensible to support use cases such as executing individual tools on containers or through a remote API.


.. _FAQ:WhatNot:

What is EDA² *not* trying to solve?
===================================

Providing a ready-to-use solution for end-users is not in the scope of EDA².
That is, implementations of layer *Workflows* are all expected to be external.
There might be some integration tests in the EDA² repositories which combine multiple layers; however, supporting
user-input to waveform/bitstream tasks is to be done in other repositories.

By the same token, unique features provided by existing frameworks are out of scope:

* Python testbenches to wrap HDL UUTs through VPI/VHPI are supported by CoCoTb.
* JSON based configuration files are supported by Edalize.
* YAML based configuration files are supported by FuseSoC.
* Downloading dependencies is supported by FuseSoC.
* Defining multiple tests in a single HDL testbench is supported by VUnit.
* Incremental compilation is supported by VUnit.
* Verification Components are provided by CoCoTb, OSVVM, UVVM, VUnit, etc.
* Homogeneous compile/run/synth commands/functions are provided by all other frameworks.


.. _FAQ:IsReady:

Is EDA² ready to be used?
=========================

Some layers of EDA² are ready to be used, reviewed and improved, while others are expected to be developed during 2022.

* End-users which need integral ready-to-use solutions at the moment are encouraged to evaluate existing projects
  listed in :ref:`EDAA:Workflows`.
* Developers who are maintaining existing workflows are invited to review EDA² and to engage in the enhancements to make
  layers suit their needs.
  Existing workflows can be in-house plumbing and/or custom complex workflows (probably out of reach of existing
  solutions).

The following layers are usable already, and open to improvements/contributions:

* :doc:`pyEDAA.ProjectModel ➚ <projectmodel:index>`
* :doc:`pyVHDLModel ➚ <vhdlmodel:index>`

  * :doc:`GHDL ➚ <ghdl:index>`: :mod:`ghdl:pyGHDL.dom`

* :doc:`pySVModel ➚ <svmodel:index>`
* :doc:`pyEDAA.IPXACT ➚ <ipxact:index>`

Other layers are work in progress:

* :doc:`pyEDAA.CLITool ➚ <clitool:index>`
* :doc:`pyEDAA.OutputFilter ➚ <outputfilter:index>`
* :doc:`pyEDAA.Reports ➚ <reports:index>`
* :doc:`pyEDAA.UCIS ➚ <ucis:index>`
* :doc:`pyEDAA.Launcher ➚ <launcher:index>`

Overall, it is a mid-term project to build EDA² and the community around it.
Since there are so many open source Python projects to deal with EDA workflows, the development of EDA² is not focused
on reimplementing the workflows or achieving results for end-users fast.
Instead, the main purpose is to improve code reuse and interoperability, primarily among maintainers of existing
workflows.


.. _FAQ:Audience:

What is the target audience of EDA²?
====================================

EDA² is focused on developers who maintain or develop Python codebases to deal with EDA tooling.
The reference implementation of all the layers is written in Python, using type hints and docstrings for robustness and
automatic documentation generation.
Moreover, classes are used for better organisation/encapsulation, which allows auto-generating dot diagrams of class
relationships to be included in the documentation.
Classes represent the semantics of the domains modeled by each abstraction layer.

Therefore, EDA² is not expected to be used by end-users to get a bitstream or a waveform from a bunch of HDL sources.
Instead, it is targeting tool developers who are to provide the workflows for end-users to achieve their goals.
Intrepid users are nonetheless invited to build their ad-hoc workflows by combining EDA² layers.


.. _FAQ:Examples:

Where are the examples/demos?
=============================

Each EDA² repository contains, at least, some unit tests (typically in subdir ``tests``) and a minimal working example
(MWE) in the README.
The MWE is extracted from the README and tested in the CI pipeline.

Some of the layers are already being used in other repositories:

* pyVHDLModel:

  * :mod:`ghdl:pyGHDL.dom` uses GHDL's ``libghdl`` and :mod:`ghdl:pyGHDL.libghdl` as a frontend for pyVHDLModel.
  * :ref:`Open Source Verification Bundle <osvb:API:Project>` provides :ref:`osvb:API:Project:pyVHDLModelUtils`, based
    on pyGHDL.dom.

    * :ref:`osvb:API:Project:OSVDE`
    * :ref:`osvb:API:Project:DocGen`

Further examples and tests are work in progress.
Let us know if you want to contribute!


.. _FAQ:VUnit:

Is EDA² based on VUnit?
=======================

EDA²'s ProjectModel and CLITool are mostly based on pyIPCMI, which was split from Pile-Of-Cores (PoC).

In :doc:`osvb:index`, VUnit is used as the root of the discussion about combining existing open source HDL Verification
frameworks/methodologies.
Some of the documentation in EDA² was first written in OSVB and then moved, which might be misleading.
Anyway, OSVB is focused on simulation and co-simulation only; it is, thus, a subset of EDA².
Supporting synthesis is out of scope of VUnit.


.. _FAQ:existingusers:

What do users of existing frameworks gain using EDA²?
=====================================================

Existing frameworks such as FuseSoC/Edalize, VUnit or CoCoTb transitioning to using EDA² should be transparent for
end-users, except with regard to the required python dependencies (modules).
See :ref:`FAQ:Audience`.
