import qiskit_metal as metal
from qiskit_metal import designs, draw
from qiskit_metal import MetalGUI, Dict, Headings

design = designs.DesignPlanar({}, True)
design.chips.main.size['size_x'] = '2mm'
design.chips.main.size['size_y'] = '2mm'

# gui = MetalGUI(design)

from qiskit_metal.qlibrary.qubits.transmon_pocket import TransmonPocket

design.delete_all_components()

q1 = TransmonPocket(
    design,
    'Q1',
    options=dict(pad_width='425 um',
                 pocket_height='650um',
                 connection_pads=dict(
                     readout=dict(loc_W=+1, loc_H=+1, pad_width='200um'))))

# gui.rebuild()
