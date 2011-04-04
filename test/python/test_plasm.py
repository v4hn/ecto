#!/usr/bin/env python
import ecto
#from ecto.doc import print_module_doc
import buster

def test_plasm():
    scatter = ecto.make(buster.Scatter, n=3, x=3)
    gather = ecto.make(buster.Gather, n=3)
#    printer = ecto.make(buster.Printer)
#    ecto.print_module_doc(scatter)
#    ecto.print_module_doc(gather)
    print "#################\nPlasm test\n#################"
    plasm = ecto.Plasm()
    for f, t in zip(ecto.keys(scatter.outputs), ecto.keys(gather.inputs)):
            plasm.connect(scatter, f, gather, t)
    plasm.go(gather)
    result = gather.o.out.get()
    print "gather out (should be 9):", result
    assert(result == 9)
    print plasm.viz()
    print plasm.vertices()
    print plasm.edges()
    ecto.view_plasm(plasm)
    pm = plasm.toModule([scatter],[gather])
    ecto.print_module_doc(pm)
    

if __name__ == '__main__':
    test_plasm()




