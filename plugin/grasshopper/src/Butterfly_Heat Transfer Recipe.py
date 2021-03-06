# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Butterfly; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Heat Transfer Recipe.

-

    Args:
        _turbulenceProp_: Turbulence properties. This values will overwrite default
            values, and can be updated while the solution is running.
        _temperature_: Reference temperature in degrees celsius. Default is set to
            26.85 C (300 K) degrees.
        fvSchemes_: Optional input for fvSchemes to overwrite default fvSchemes.
        fvSolution_: Optional input for fvSolution to overwrite default fvSolution.
        residualControl_: residualControl values. This values will overwrite default
            values, and can be updated while the solution is running.
        _relaxationFactors_: relaxationFactors. This values will overwrite default
            values, and can be updated while the solution is running.
    Returns:
        readMe!: Reports, errors, warnings, etc.
        case: Butterfly case.
"""

ghenv.Component.Name = "Butterfly_Heat Transfer Recipe"
ghenv.Component.NickName = "heatTransfer"
ghenv.Component.Message = 'VER 0.0.04\nNOV_22_2017'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "05::Recipe"
ghenv.Component.AdditionalHelpFromDocStrings = "1"

try:
    from butterfly.recipe import HeatTransfer
except ImportError as e:
    msg = '\nFailed to import butterfly:'
    raise ImportError('{}\n{}'.format(msg, e))

if _temperature_:
    _temperature_ += 273.15

recipe = HeatTransfer(_turbulenceProp_, fvSchemes_, fvSolution_, residualControl_,
                      _relaxationFactors_, TRef=_temperature_)

