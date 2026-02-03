# ./_for.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:955b1fbe7f57bbcbaffe010cf7c68604bdea055e
# Generated 2026-02-02 18:03:54.409769 by PyXB version 1.2.6 using Python 3.14.0.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3 [xmlns:for]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:c741fc79-0a5d-4071-ac2f-90019036e17c')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import _ct as _ImportedBinding__ct
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, fallback_namespace=None, location_base=None, default_namespace=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=fallback_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 40, 5)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON)
STD_ANON.P = STD_ANON._CF_enumeration.addEnumeration(unicode_value='P', tag='P')
STD_ANON.A = STD_ANON._CF_enumeration.addEnumeration(unicode_value='A', tag='A')
STD_ANON.M = STD_ANON._CF_enumeration.addEnumeration(unicode_value='M', tag='M')
STD_ANON._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(1))
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration,
   STD_ANON._CF_length)
_module_typeBindings.STD_ANON = STD_ANON

# Complex type {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}PlatformData with content type SIMPLE
class PlatformData (pyxb.binding.basis.complexTypeDefinition):
    """Platform number with associated flags"""
    _TypeDefinition = _ImportedBinding__ct.PlatformType
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PlatformData')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 20, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding__ct.PlatformType
    
    # Attribute platsup uses Python identifier platsup
    __platsup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'platsup'), 'platsup', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_PlatformData_platsup', pyxb.binding.datatypes.boolean, unicode_default='false')
    __platsup._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 26, 4)
    __platsup._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 26, 4)
    
    platsup = property(__platsup.value, __platsup.set, None, 'Platform number is suppressed and should not be displayed.')

    
    # Attribute cisPlatsup uses Python identifier cisPlatsup
    __cisPlatsup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cisPlatsup'), 'cisPlatsup', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_PlatformData_cisPlatsup', pyxb.binding.datatypes.boolean, unicode_default='false')
    __cisPlatsup._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 31, 4)
    __cisPlatsup._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 31, 4)
    
    cisPlatsup = property(__cisPlatsup.value, __cisPlatsup.set, None, 'Whether a CIS, or Darwin Workstation, has set platform suppression at this location.')

    
    # Attribute platsrc uses Python identifier platsrc
    __platsrc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'platsrc'), 'platsrc', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_PlatformData_platsrc', _module_typeBindings.STD_ANON, unicode_default='P')
    __platsrc._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 36, 4)
    __platsrc._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 36, 4)
    
    platsrc = property(__platsrc.value, __platsrc.set, None, 'The source of the platfom number. P = Planned, A = Automatic, M = Manual.')

    
    # Attribute conf uses Python identifier conf
    __conf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'conf'), 'conf', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_PlatformData_conf', pyxb.binding.datatypes.boolean, unicode_default='false')
    __conf._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 49, 4)
    __conf._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 49, 4)
    
    conf = property(__conf.value, __conf.set, None, 'True if the platform number is confirmed.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __platsup.name() : __platsup,
        __cisPlatsup.name() : __cisPlatsup,
        __platsrc.name() : __platsrc,
        __conf.name() : __conf
    })
_module_typeBindings.PlatformData = PlatformData
Namespace.addCategoryObject('typeBinding', 'PlatformData', PlatformData)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}TSTimeData with content type EMPTY
class TSTimeData (pyxb.binding.basis.complexTypeDefinition):
    """Type describing time-based forecast attributes for a TS arrival/departure/pass"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSTimeData')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 57, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute et uses Python identifier et
    __et = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'et'), 'et', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSTimeData_et', _ImportedBinding__ct.RTTITimeType)
    __et._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 61, 2)
    __et._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 61, 2)
    
    et = property(__et.value, __et.set, None, 'Estimated Time. For locations that are public stops, this will be based on the "public schedule". For operational stops and passing locations, it will be based on the "working schedule". It is only published where there is a corresponding "activity" for the service.')

    
    # Attribute wet uses Python identifier wet
    __wet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wet'), 'wet', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSTimeData_wet', _ImportedBinding__ct.RTTITimeType)
    __wet._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 66, 2)
    __wet._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 66, 2)
    
    wet = property(__wet.value, __wet.set, None, 'The estimated time based on the "working schedule". This will only be set for public stops when (i) it also differs from the estimated time based on the "public schedule", or (ii) where there is an operational "activity" but no public "activity".')

    
    # Attribute at uses Python identifier at
    __at = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'at'), 'at', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSTimeData_at', _ImportedBinding__ct.RTTITimeType)
    __at._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 71, 2)
    __at._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 71, 2)
    
    at = property(__at.value, __at.set, None, 'Actual Time')

    
    # Attribute atRemoved uses Python identifier atRemoved
    __atRemoved = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'atRemoved'), 'atRemoved', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSTimeData_atRemoved', pyxb.binding.datatypes.boolean, unicode_default='false')
    __atRemoved._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 76, 2)
    __atRemoved._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 76, 2)
    
    atRemoved = property(__atRemoved.value, __atRemoved.set, None, 'If true, indicates that an actual time ("at") value has just been removed and replaced by an estimated time ("et"). Note that this attribute will only be set to "true" once, when the actual time is removed, and will not be set in any snapshot.')

    
    # Attribute atClass uses Python identifier atClass
    __atClass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'atClass'), 'atClass', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSTimeData_atClass', pyxb.binding.datatypes.string)
    __atClass._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 81, 2)
    __atClass._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 81, 2)
    
    atClass = property(__atClass.value, __atClass.set, None, 'The class of the actual time.')

    
    # Attribute etmin uses Python identifier etmin
    __etmin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'etmin'), 'etmin', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSTimeData_etmin', _ImportedBinding__ct.RTTITimeType)
    __etmin._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 86, 2)
    __etmin._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 86, 2)
    
    etmin = property(__etmin.value, __etmin.set, None, 'The manually applied lower limit that has been applied to the estimated time at this location. The estimated time will not be set lower than this value, but may be set higher.')

    
    # Attribute etUnknown uses Python identifier etUnknown
    __etUnknown = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'etUnknown'), 'etUnknown', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSTimeData_etUnknown', pyxb.binding.datatypes.boolean, unicode_default='false')
    __etUnknown._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 91, 2)
    __etUnknown._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 91, 2)
    
    etUnknown = property(__etUnknown.value, __etUnknown.set, None, 'Indicates that an unknown delay forecast has been set for the estimated time at this location. Note that this value indicates where a manual unknown delay forecast has been set, whereas it is the "delayed" attribute that indicates that the actual forecast is "unknown delay".')

    
    # Attribute delayed uses Python identifier delayed
    __delayed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'delayed'), 'delayed', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSTimeData_delayed', pyxb.binding.datatypes.boolean, unicode_default='false')
    __delayed._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 96, 2)
    __delayed._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 96, 2)
    
    delayed = property(__delayed.value, __delayed.set, None, 'Indicates that this estimated time is a forecast of "unknown delay". Displayed  as "Delayed" in LDB. Note that this value indicates that this forecast is "unknown delay", whereas it is the "etUnknown" attribute that indicates where the manual unknown delay forecast has been set.')

    
    # Attribute src uses Python identifier src
    __src = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'src'), 'src', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSTimeData_src', pyxb.binding.datatypes.string)
    __src._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 101, 2)
    __src._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 101, 2)
    
    src = property(__src.value, __src.set, None, 'The source of the forecast or actual time.')

    
    # Attribute srcInst uses Python identifier srcInst
    __srcInst = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srcInst'), 'srcInst', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSTimeData_srcInst', _ImportedBinding__ct.SourceTypeInst)
    __srcInst._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 106, 2)
    __srcInst._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 106, 2)
    
    srcInst = property(__srcInst.value, __srcInst.set, None, 'The RTTI CIS code of the CIS instance if the src is a CIS.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __et.name() : __et,
        __wet.name() : __wet,
        __at.name() : __at,
        __atRemoved.name() : __atRemoved,
        __atClass.name() : __atClass,
        __etmin.name() : __etmin,
        __etUnknown.name() : __etUnknown,
        __delayed.name() : __delayed,
        __src.name() : __src,
        __srcInst.name() : __srcInst
    })
_module_typeBindings.TSTimeData = TSTimeData
Namespace.addCategoryObject('typeBinding', 'TSTimeData', TSTimeData)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}TSLocation with content type ELEMENT_ONLY
class TSLocation (pyxb.binding.basis.complexTypeDefinition):
    """Forecast data for an individual location in the service's schedule"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSLocation')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 112, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}arr uses Python identifier arr
    __arr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'arr'), 'arr', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_httpwww_thalesgroup_comrttiPushPortForecastsv3arr', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 117, 3), )

    
    arr = property(__arr.value, __arr.set, None, 'Forecast data for the arrival at this location')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}dep uses Python identifier dep
    __dep = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dep'), 'dep', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_httpwww_thalesgroup_comrttiPushPortForecastsv3dep', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 122, 3), )

    
    dep = property(__dep.value, __dep.set, None, 'Forecast data for the departure at this location')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}pass uses Python identifier pass_
    __pass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pass'), 'pass_', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_httpwww_thalesgroup_comrttiPushPortForecastsv3pass', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 127, 3), )

    
    pass_ = property(__pass.value, __pass.set, None, 'Forecast data for the pass of this location')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}plat uses Python identifier plat
    __plat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'plat'), 'plat', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_httpwww_thalesgroup_comrttiPushPortForecastsv3plat', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 132, 3), )

    
    plat = property(__plat.value, __plat.set, None, 'Current platform number')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}suppr uses Python identifier suppr
    __suppr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'suppr'), 'suppr', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_httpwww_thalesgroup_comrttiPushPortForecastsv3suppr', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 137, 3), )

    
    suppr = property(__suppr.value, __suppr.set, None, 'The service is suppressed at this location.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}length uses Python identifier length
    __length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'length'), 'length', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_httpwww_thalesgroup_comrttiPushPortForecastsv3length', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 142, 3), )

    
    length = property(__length.value, __length.set, None, 'The length of the service at this location on departure (or arrival at destination). The default value of zero indicates that the length is unknown.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}detachFront uses Python identifier detachFront
    __detachFront = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'detachFront'), 'detachFront', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_httpwww_thalesgroup_comrttiPushPortForecastsv3detachFront', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 147, 3), )

    
    detachFront = property(__detachFront.value, __detachFront.set, None, 'Indicates from which end of the train stock will be detached. The value is set to “true” if stock will be detached from the front of the train at this location. It will be set at each location where stock will be detached from the front. Darwin will not validate that a stock detachment activity code applies at this location.')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_wta', _ImportedBinding__ct.WTimeType)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 243, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 243, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working time of arrival.')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_wtd', _ImportedBinding__ct.WTimeType)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 248, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 248, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working time of departure.')

    
    # Attribute wtp uses Python identifier wtp
    __wtp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtp'), 'wtp', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_wtp', _ImportedBinding__ct.WTimeType)
    __wtp._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 253, 2)
    __wtp._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 253, 2)
    
    wtp = property(__wtp.value, __wtp.set, None, 'Working time of pass.')

    
    # Attribute pta uses Python identifier pta
    __pta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pta'), 'pta', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_pta', _ImportedBinding__ct.RTTITimeType)
    __pta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 258, 2)
    __pta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 258, 2)
    
    pta = property(__pta.value, __pta.set, None, 'Public time of arrival.')

    
    # Attribute ptd uses Python identifier ptd
    __ptd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ptd'), 'ptd', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_ptd', _ImportedBinding__ct.RTTITimeType)
    __ptd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 263, 2)
    __ptd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 263, 2)
    
    ptd = property(__ptd.value, __ptd.set, None, 'Public time of departure.')

    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TSLocation_tpl', _ImportedBinding__ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 153, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 153, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    _ElementMap.update({
        __arr.name() : __arr,
        __dep.name() : __dep,
        __pass.name() : __pass,
        __plat.name() : __plat,
        __suppr.name() : __suppr,
        __length.name() : __length,
        __detachFront.name() : __detachFront
    })
    _AttributeMap.update({
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __wtp.name() : __wtp,
        __pta.name() : __pta,
        __ptd.name() : __ptd,
        __tpl.name() : __tpl
    })
_module_typeBindings.TSLocation = TSLocation
Namespace.addCategoryObject('typeBinding', 'TSLocation', TSLocation)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}TS with content type ELEMENT_ONLY
class TS (pyxb.binding.basis.complexTypeDefinition):
    """Train Status. Update to the "real time" forecast data for a service."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TS')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 160, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}LateReason uses Python identifier LateReason
    __LateReason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LateReason'), 'LateReason', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TS_httpwww_thalesgroup_comrttiPushPortForecastsv3LateReason', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 165, 3), )

    
    LateReason = property(__LateReason.value, __LateReason.set, None, 'Late running reason for this service. The reason applies to all locations of this service.')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3}Location uses Python identifier Location
    __Location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Location'), 'Location', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TS_httpwww_thalesgroup_comrttiPushPortForecastsv3Location', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 170, 3), )

    
    Location = property(__Location.value, __Location.set, None, "Update of forecast data for an individual location in the service's schedule")

    
    # Attribute rid uses Python identifier rid
    __rid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rid'), 'rid', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TS_rid', _ImportedBinding__ct.RIDType, required=True)
    __rid._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 176, 2)
    __rid._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 176, 2)
    
    rid = property(__rid.value, __rid.set, None, 'RTTI unique Train Identifier')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TS_uid', _ImportedBinding__ct.UIDType, required=True)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 181, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 181, 2)
    
    uid = property(__uid.value, __uid.set, None, 'Train UID')

    
    # Attribute ssd uses Python identifier ssd
    __ssd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ssd'), 'ssd', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TS_ssd', _ImportedBinding__ct.RTTIDateType, required=True)
    __ssd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 186, 2)
    __ssd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 186, 2)
    
    ssd = property(__ssd.value, __ssd.set, None, 'Scheduled Start Date')

    
    # Attribute isReverseFormation uses Python identifier isReverseFormation
    __isReverseFormation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isReverseFormation'), 'isReverseFormation', '__httpwww_thalesgroup_comrttiPushPortForecastsv3_TS_isReverseFormation', pyxb.binding.datatypes.boolean, unicode_default='false')
    __isReverseFormation._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 191, 2)
    __isReverseFormation._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 191, 2)
    
    isReverseFormation = property(__isReverseFormation.value, __isReverseFormation.set, None, 'Indicates whether a train that divides is working with portions in reverse to their normal formation. The value applies to the whole train. Darwin will not validate that a divide association actually exists for this service.')

    _ElementMap.update({
        __LateReason.name() : __LateReason,
        __Location.name() : __Location
    })
    _AttributeMap.update({
        __rid.name() : __rid,
        __uid.name() : __uid,
        __ssd.name() : __ssd,
        __isReverseFormation.name() : __isReverseFormation
    })
_module_typeBindings.TS = TS
Namespace.addCategoryObject('typeBinding', 'TS', TS)




TSLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'arr'), TSTimeData, scope=TSLocation, documentation='Forecast data for the arrival at this location', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 117, 3)))

TSLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dep'), TSTimeData, scope=TSLocation, documentation='Forecast data for the departure at this location', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 122, 3)))

TSLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pass'), TSTimeData, scope=TSLocation, documentation='Forecast data for the pass of this location', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 127, 3)))

TSLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'plat'), PlatformData, scope=TSLocation, documentation='Current platform number', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 132, 3)))

TSLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'suppr'), pyxb.binding.datatypes.boolean, scope=TSLocation, documentation='The service is suppressed at this location.', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 137, 3), unicode_default='false'))

TSLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'length'), _ImportedBinding__ct.TrainLengthType, scope=TSLocation, documentation='The length of the service at this location on departure (or arrival at destination). The default value of zero indicates that the length is unknown.', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 142, 3), unicode_default='0'))

TSLocation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'detachFront'), pyxb.binding.datatypes.boolean, scope=TSLocation, documentation='Indicates from which end of the train stock will be detached. The value is set to “true” if stock will be detached from the front of the train at this location. It will be set at each location where stock will be detached from the front. Darwin will not validate that a stock detachment activity code applies at this location.', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 147, 3), unicode_default='false'))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 117, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 122, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 127, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 132, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 137, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 142, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 147, 3))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'arr')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 117, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dep')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 122, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pass')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 127, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'plat')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 132, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'suppr')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 137, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'length')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 142, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(TSLocation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'detachFront')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 147, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TSLocation._Automaton = _BuildAutomaton()




TS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LateReason'), _ImportedBinding__ct.DisruptionReasonType, scope=TS, documentation='Late running reason for this service. The reason applies to all locations of this service.', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 165, 3)))

TS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Location'), TSLocation, scope=TS, documentation="Update of forecast data for an individual location in the service's schedule", location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 170, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 165, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 170, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LateReason')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 165, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Location')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTForecasts_v3.xsd', 170, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TS._Automaton = _BuildAutomaton_()

