# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Set meshing parameters for blockMesh and snappyHexMesh.


    Args:
        _cellSizeXYZ_: Cell size in (x, y, z) as a tuple (default: length / 5).
            This value updates number of divisions in blockMeshDict.
        _gradXYZ_: A simpleGrading (default: simpleGrading(1, 1, 1)). This value
            updates grading in blockMeshDict.
        _locationInMesh_: A tuple for the location of the mesh to be kept. This
            value updates locationInMesh in snappyHexMeshDict.
        _globRefineLevel_: A tuple of (min, max) values for global refinment.
            This value updates globalRefinementLevel in snappyHexMeshDict.
    Returns:
        meshParams: meshingParameters.
"""

ghenv.Component.Name = "Butterfly_Meshing Parameters"
ghenv.Component.NickName = "meshParams"
ghenv.Component.Message = 'VER 0.0.04\nMAR_19_2017'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "4"

try:
    # import butterfly
    from butterfly.meshingparameters import MeshingParameters
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

# create blockMeshDict based on BBox
if _cellSizeXYZ_:
    _cellSizeXYZ_ = _cellSizeXYZ_.X, _cellSizeXYZ_.Y, _cellSizeXYZ_.Z

meshParams = MeshingParameters(
    _cellSizeXYZ_, _gradXYZ_, _locationInMesh_, _globRefineLevel_)
