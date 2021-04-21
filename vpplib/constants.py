from os import PRIO_PGRP


VERSION = "0.1.0"

PROJECT_CONFIG_FILE_NAME = "Vpp.toml"
VPP_DESC_FILE = "Vpp_files.json"

SOURCE_DIR = "src"

MODULE_TEMPLATE = """module moduleNamePlaceholder (
);
    
endmodule"""

MODULE_NAME_PLACEHOLDER="moduleNamePlaceholder"

TEST_MODULE_TEMPLATE = """`timescale 1ps/1ps
module testModulePlaceholder ();
moduleNamePlaceholder moduleNamePlaceholder_instance(
);
reg clk;

initial begin
   $dumpfile("testModulePlaceholder.vcd");
   $dumpvars;
   #1000 $finish;
end


initial begin
clk=0;
end


always begin
#10 clk=~clk;
end

endmodule"""

TEST_MODULE_NAME_PLACEHOLDER="testModulePlaceholder"