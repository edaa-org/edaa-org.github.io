.. _EDAA:Workflows:

Workflows and integration
#########################

The following projects are all written in Python and were all created and developed during the last decade:

* :awesome:`CoCoTb <cocotb>` (2013)
* :awesome:`Pile of Cores Library (PoC) <poc>` (2014)
* :awesome:`VUnit <vunit>` (2014)
* :awesome:`SymbiFlow <symbiflow>` (2017)
* :awesome:`Edalize <edalize>` (2018), split from :awesome:`FuseSoC <fusesoc>` (2011)
* :awesome:`tsfpga <tsfpga>` (2018)
* :awesome:`pyFPGA <pyfpga>` (2019), based on fpga_helpers (2015)
* :awesome:`Xeda <xeda>` (2020)
* :awesome:`SiliconCompiler <siliconcompiler>` (2021)
* :awesome:`legoHDL <legohdl>` (2021)

All of them implement multiple of the layers in the EDAA Model, however, most of them were not written with reusabillity
in mind.
Hopefully, maintainers of those projects will be willing to isolate the reusable pieces of their codebases, so they can
focus their effort on the features unique to their solution.
The following is our wishlist:

* CoCoTb (to be analysed yet)

* PoC/pyIPCMI

  * Abstraction for EDA tool tasks.
  * Abstraction for post-processing the logs.
  * Abstraction of a Project.

* VUnit

  * Switching simulator with an environment variable.
  * Wildcards support and as-easy-as-possible API for defining filesets (sources, libs, etc.).
  * Dependency scanning and incremental compilation.

    * Dependency scanning features might be provided by pyVHDLModelUtils, instead of having it implemented in VUnit's
      codebase.

  * Integration between Python and the HDL runner.

    * Interpretation of what a success/failure is (specific for each VHDL revision).
    * Definition of multiple tests in VHDL and management of which to execute.
    * Complex generics, JSON-for-VHDL, configurations, etc.

* FuseSoC/Edalize

  * ``.core`` file format and all the projects which use it already.
  * Specific know-how about the less mainstream toolchains.
  * Support for fine-grained containers.

* SymbiFlow (to be analysed yet)

* tsfpga (to be analysed yet)

* pyFPGA

  * Similarly to fusesoc/edalize, specific know-how about some toolchains/flows and support for fine-grained containers.
  * Easy Python API for defining the sources, libs, targets, etc. for synthesis.

* Xeda (to be analysed yet)

* SiliconCompiler (to be analysed yet)

* legoHDL (to be analysed yet)


.. toctree::
   :hidden:

   CoCoTb
   FuseSoCEdalize
   legoHDL
   PyFPGA
   pyIPCMI
   SiliconCompiler
   SymbiFlow
   tsfpga
   VUnit
   Xeda
