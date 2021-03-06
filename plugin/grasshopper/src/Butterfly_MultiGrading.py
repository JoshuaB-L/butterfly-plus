# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
MultiGrading
Create a grading for multiple segmentGradings.

-

    Args:
        _segmentGradings: A list of segmentGradings.
        
    Returns:
        grading: A butterfly Grading. Connect the output to gradXYZ component to
            set the grading of blockMesh in X, Y or Z direction.
"""

ghenv.Component.Name = "Butterfly_MultiGrading"
ghenv.Component.NickName = "multiGrading"
ghenv.Component.Message = 'VER 0.0.04\nMAR_14_2017'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "03::Mesh"
ghenv.Component.AdditionalHelpFromDocStrings = "3"

try:
    from butterfly.grading import MultiGrading
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _segmentGradings:
    grading = MultiGrading(_segmentGradings)
