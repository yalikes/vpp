`timescale 1ps/1ps
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

endmodule