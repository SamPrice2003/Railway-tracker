# ./_sch2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:669a15115efa83db44f88842893e43a1581c70a0
# Generated 2026-02-02 18:03:54.409260 by PyXB version 1.2.6 using Python 3.14.0.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/Schedules/v2 [xmlns:sch2]

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
import _ct2 as _ImportedBinding__ct2
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/Schedules/v2', create_if_missing=True)
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


# Atomic simple type: {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}CategoryType
class CategoryType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Association Category Type: JJ=Join, VV=Split, LK=Linked, NP=Next-Working"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CategoryType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 18, 1)
    _Documentation = 'Association Category Type: JJ=Join, VV=Split, LK=Linked, NP=Next-Working'
CategoryType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=CategoryType)
CategoryType.JJ = CategoryType._CF_enumeration.addEnumeration(unicode_value='JJ', tag='JJ')
CategoryType.VV = CategoryType._CF_enumeration.addEnumeration(unicode_value='VV', tag='VV')
CategoryType.LK = CategoryType._CF_enumeration.addEnumeration(unicode_value='LK', tag='LK')
CategoryType.NP = CategoryType._CF_enumeration.addEnumeration(unicode_value='NP', tag='NP')
CategoryType._InitializeFacetMap(CategoryType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'CategoryType', CategoryType)
_module_typeBindings.CategoryType = CategoryType

# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}AssocService with content type EMPTY
class AssocService (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}AssocService with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AssocService')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 30, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_AssocService_wta', _ImportedBinding__ct.WTimeType)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 243, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 243, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working time of arrival.')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_AssocService_wtd', _ImportedBinding__ct.WTimeType)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 248, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 248, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working time of departure.')

    
    # Attribute wtp uses Python identifier wtp
    __wtp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtp'), 'wtp', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_AssocService_wtp', _ImportedBinding__ct.WTimeType)
    __wtp._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 253, 2)
    __wtp._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 253, 2)
    
    wtp = property(__wtp.value, __wtp.set, None, 'Working time of pass.')

    
    # Attribute pta uses Python identifier pta
    __pta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pta'), 'pta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_AssocService_pta', _ImportedBinding__ct.RTTITimeType)
    __pta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 258, 2)
    __pta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 258, 2)
    
    pta = property(__pta.value, __pta.set, None, 'Public time of arrival.')

    
    # Attribute ptd uses Python identifier ptd
    __ptd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ptd'), 'ptd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_AssocService_ptd', _ImportedBinding__ct.RTTITimeType)
    __ptd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 263, 2)
    __ptd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTCommonTypes_v1.xsd', 263, 2)
    
    ptd = property(__ptd.value, __ptd.set, None, 'Public time of departure.')

    
    # Attribute rid uses Python identifier rid
    __rid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rid'), 'rid', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_AssocService_rid', _ImportedBinding__ct.RIDType, required=True)
    __rid._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 31, 2)
    __rid._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 31, 2)
    
    rid = property(__rid.value, __rid.set, None, 'RTTI Train ID. Note that since this is an RID, the service must already exist within Darwin.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __wtp.name() : __wtp,
        __pta.name() : __pta,
        __ptd.name() : __ptd,
        __rid.name() : __rid
    })
_module_typeBindings.AssocService = AssocService
Namespace.addCategoryObject('typeBinding', 'AssocService', AssocService)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}Association with content type ELEMENT_ONLY
class Association (pyxb.binding.basis.complexTypeDefinition):
    """Type describing an association between schedules"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Association')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 42, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}main uses Python identifier main
    __main = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'main'), 'main', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Association_httpwww_thalesgroup_comrttiPushPortSchedulesv2main', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 47, 3), )

    
    main = property(__main.value, __main.set, None, 'The through, previous working or link-to service')

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}assoc uses Python identifier assoc
    __assoc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'assoc'), 'assoc', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Association_httpwww_thalesgroup_comrttiPushPortSchedulesv2assoc', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 52, 3), )

    
    assoc = property(__assoc.value, __assoc.set, None, 'The starting, terminating, subsequent working or link-from service')

    
    # Attribute tiploc uses Python identifier tiploc
    __tiploc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tiploc'), 'tiploc', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Association_tiploc', _ImportedBinding__ct.TiplocType, required=True)
    __tiploc._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 58, 2)
    __tiploc._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 58, 2)
    
    tiploc = property(__tiploc.value, __tiploc.set, None, 'The TIPLOC of the location where the association occurs.')

    
    # Attribute category uses Python identifier category
    __category = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'category'), 'category', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Association_category', _module_typeBindings.CategoryType, required=True)
    __category._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 63, 2)
    __category._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 63, 2)
    
    category = property(__category.value, __category.set, None, 'Association category')

    
    # Attribute isCancelled uses Python identifier isCancelled
    __isCancelled = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isCancelled'), 'isCancelled', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Association_isCancelled', pyxb.binding.datatypes.boolean, unicode_default='false')
    __isCancelled._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 68, 2)
    __isCancelled._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 68, 2)
    
    isCancelled = property(__isCancelled.value, __isCancelled.set, None, 'True if this association is cancelled, i.e. the association exists but will no longer happen.')

    
    # Attribute isDeleted uses Python identifier isDeleted
    __isDeleted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isDeleted'), 'isDeleted', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Association_isDeleted', pyxb.binding.datatypes.boolean, unicode_default='false')
    __isDeleted._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 73, 2)
    __isDeleted._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 73, 2)
    
    isDeleted = property(__isDeleted.value, __isDeleted.set, None, 'True if this association is deleted, i.e. the association no longer exists.')

    _ElementMap.update({
        __main.name() : __main,
        __assoc.name() : __assoc
    })
    _AttributeMap.update({
        __tiploc.name() : __tiploc,
        __category.name() : __category,
        __isCancelled.name() : __isCancelled,
        __isDeleted.name() : __isDeleted
    })
_module_typeBindings.Association = Association
Namespace.addCategoryObject('typeBinding', 'Association', Association)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}OR with content type EMPTY
class OR (pyxb.binding.basis.complexTypeDefinition):
    """Defines a Passenger Origin Calling Point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OR')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 119, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OR_tpl', _ImportedBinding__ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OR_act', _ImportedBinding__ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OR_planAct', _ImportedBinding__ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OR_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute pta uses Python identifier pta
    __pta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pta'), 'pta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OR_pta', _ImportedBinding__ct.RTTITimeType)
    __pta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 108, 2)
    __pta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 108, 2)
    
    pta = property(__pta.value, __pta.set, None, 'Public Scheduled Time of Arrival')

    
    # Attribute ptd uses Python identifier ptd
    __ptd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ptd'), 'ptd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OR_ptd', _ImportedBinding__ct.RTTITimeType)
    __ptd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 113, 2)
    __ptd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 113, 2)
    
    ptd = property(__ptd.value, __ptd.set, None, 'Public Scheduled Time of Departure')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OR_wta', _ImportedBinding__ct.WTimeType)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 125, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 125, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working Scheduled Time of Arrival')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OR_wtd', _ImportedBinding__ct.WTimeType, required=True)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 130, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 130, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working Scheduled Time of Departure')

    
    # Attribute fd uses Python identifier fd
    __fd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fd'), 'fd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OR_fd', _ImportedBinding__ct.TiplocType)
    __fd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 135, 2)
    __fd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 135, 2)
    
    fd = property(__fd.value, __fd.set, None, 'TIPLOC of False Destination to be used at this location')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __pta.name() : __pta,
        __ptd.name() : __ptd,
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __fd.name() : __fd
    })
_module_typeBindings.OR = OR
Namespace.addCategoryObject('typeBinding', 'OR', OR)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}OPOR with content type EMPTY
class OPOR (pyxb.binding.basis.complexTypeDefinition):
    """Defines an Operational Origin Calling Point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OPOR')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 141, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPOR_tpl', _ImportedBinding__ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPOR_act', _ImportedBinding__ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPOR_planAct', _ImportedBinding__ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPOR_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPOR_wta', _ImportedBinding__ct.WTimeType)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 146, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 146, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working Scheduled Time of Arrival')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPOR_wtd', _ImportedBinding__ct.WTimeType, required=True)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 151, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 151, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working Scheduled Time of Departure')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __wta.name() : __wta,
        __wtd.name() : __wtd
    })
_module_typeBindings.OPOR = OPOR
Namespace.addCategoryObject('typeBinding', 'OPOR', OPOR)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}IP with content type EMPTY
class IP (pyxb.binding.basis.complexTypeDefinition):
    """Defines aPassenger Intermediate Calling Point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IP')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 157, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_IP_tpl', _ImportedBinding__ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_IP_act', _ImportedBinding__ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_IP_planAct', _ImportedBinding__ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_IP_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute pta uses Python identifier pta
    __pta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pta'), 'pta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_IP_pta', _ImportedBinding__ct.RTTITimeType)
    __pta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 108, 2)
    __pta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 108, 2)
    
    pta = property(__pta.value, __pta.set, None, 'Public Scheduled Time of Arrival')

    
    # Attribute ptd uses Python identifier ptd
    __ptd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ptd'), 'ptd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_IP_ptd', _ImportedBinding__ct.RTTITimeType)
    __ptd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 113, 2)
    __ptd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 113, 2)
    
    ptd = property(__ptd.value, __ptd.set, None, 'Public Scheduled Time of Departure')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_IP_wta', _ImportedBinding__ct.WTimeType, required=True)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 163, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 163, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working Scheduled Time of Arrival')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_IP_wtd', _ImportedBinding__ct.WTimeType, required=True)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 168, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 168, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working Scheduled Time of Departure')

    
    # Attribute rdelay uses Python identifier rdelay
    __rdelay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rdelay'), 'rdelay', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_IP_rdelay', _ImportedBinding__ct.DelayValueType, unicode_default='0')
    __rdelay._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 173, 2)
    __rdelay._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 173, 2)
    
    rdelay = property(__rdelay.value, __rdelay.set, None, "A delay value that is implied by a change to the service's route. This value has been added to the forecast lateness of the service at the previous schedule location when calculating the expected lateness of arrival at this location.")

    
    # Attribute fd uses Python identifier fd
    __fd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fd'), 'fd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_IP_fd', _ImportedBinding__ct.TiplocType)
    __fd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 178, 2)
    __fd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 178, 2)
    
    fd = property(__fd.value, __fd.set, None, 'TIPLOC of False Destination to be used at this location')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __pta.name() : __pta,
        __ptd.name() : __ptd,
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __rdelay.name() : __rdelay,
        __fd.name() : __fd
    })
_module_typeBindings.IP = IP
Namespace.addCategoryObject('typeBinding', 'IP', IP)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}OPIP with content type EMPTY
class OPIP (pyxb.binding.basis.complexTypeDefinition):
    """Defines an Operational Intermediate Calling Point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OPIP')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 184, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPIP_tpl', _ImportedBinding__ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPIP_act', _ImportedBinding__ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPIP_planAct', _ImportedBinding__ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPIP_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPIP_wta', _ImportedBinding__ct.WTimeType, required=True)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 189, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 189, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working Scheduled Time of Arrival')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPIP_wtd', _ImportedBinding__ct.WTimeType, required=True)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 194, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 194, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working Scheduled Time of Departure')

    
    # Attribute rdelay uses Python identifier rdelay
    __rdelay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rdelay'), 'rdelay', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPIP_rdelay', _ImportedBinding__ct.DelayValueType, unicode_default='0')
    __rdelay._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 199, 2)
    __rdelay._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 199, 2)
    
    rdelay = property(__rdelay.value, __rdelay.set, None, "A delay value that is implied by a change to the service's route. This value has been added to the forecast lateness of the service at the previous schedule location when calculating the expected lateness of arrival at this location.")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __rdelay.name() : __rdelay
    })
_module_typeBindings.OPIP = OPIP
Namespace.addCategoryObject('typeBinding', 'OPIP', OPIP)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}PP with content type EMPTY
class PP (pyxb.binding.basis.complexTypeDefinition):
    """Defines an Intermediate Passing Point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PP')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 205, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_PP_tpl', _ImportedBinding__ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_PP_act', _ImportedBinding__ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_PP_planAct', _ImportedBinding__ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_PP_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute wtp uses Python identifier wtp
    __wtp = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtp'), 'wtp', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_PP_wtp', _ImportedBinding__ct.WTimeType, required=True)
    __wtp._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 210, 2)
    __wtp._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 210, 2)
    
    wtp = property(__wtp.value, __wtp.set, None, 'Working Scheduled Time of Passing')

    
    # Attribute rdelay uses Python identifier rdelay
    __rdelay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rdelay'), 'rdelay', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_PP_rdelay', _ImportedBinding__ct.DelayValueType, unicode_default='0')
    __rdelay._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 215, 2)
    __rdelay._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 215, 2)
    
    rdelay = property(__rdelay.value, __rdelay.set, None, "A delay value that is implied by a change to the service's route. This value has been added to the forecast lateness of the service at the previous schedule location when calculating the expected lateness of passing this location.")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __wtp.name() : __wtp,
        __rdelay.name() : __rdelay
    })
_module_typeBindings.PP = PP
Namespace.addCategoryObject('typeBinding', 'PP', PP)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}DT with content type EMPTY
class DT (pyxb.binding.basis.complexTypeDefinition):
    """Defines a Passenger Destination Calling point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DT')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 221, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_DT_tpl', _ImportedBinding__ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_DT_act', _ImportedBinding__ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_DT_planAct', _ImportedBinding__ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_DT_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute pta uses Python identifier pta
    __pta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pta'), 'pta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_DT_pta', _ImportedBinding__ct.RTTITimeType)
    __pta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 108, 2)
    __pta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 108, 2)
    
    pta = property(__pta.value, __pta.set, None, 'Public Scheduled Time of Arrival')

    
    # Attribute ptd uses Python identifier ptd
    __ptd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ptd'), 'ptd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_DT_ptd', _ImportedBinding__ct.RTTITimeType)
    __ptd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 113, 2)
    __ptd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 113, 2)
    
    ptd = property(__ptd.value, __ptd.set, None, 'Public Scheduled Time of Departure')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_DT_wta', _ImportedBinding__ct.WTimeType, required=True)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 227, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 227, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working Scheduled Time of Arrival')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_DT_wtd', _ImportedBinding__ct.WTimeType)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 232, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 232, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working Scheduled Time of Departure')

    
    # Attribute rdelay uses Python identifier rdelay
    __rdelay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rdelay'), 'rdelay', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_DT_rdelay', _ImportedBinding__ct.DelayValueType, unicode_default='0')
    __rdelay._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 237, 2)
    __rdelay._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 237, 2)
    
    rdelay = property(__rdelay.value, __rdelay.set, None, "A delay value that is implied by a change to the service's route. This value has been added to the forecast lateness of the service at the previous schedule location when calculating the expected lateness of arrival at this location.")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __pta.name() : __pta,
        __ptd.name() : __ptd,
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __rdelay.name() : __rdelay
    })
_module_typeBindings.DT = DT
Namespace.addCategoryObject('typeBinding', 'DT', DT)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}OPDT with content type EMPTY
class OPDT (pyxb.binding.basis.complexTypeDefinition):
    """Defines an Operational Destination Calling point"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OPDT')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 243, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tpl uses Python identifier tpl
    __tpl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tpl'), 'tpl', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPDT_tpl', _ImportedBinding__ct.TiplocType, required=True)
    __tpl._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    __tpl._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 83, 2)
    
    tpl = property(__tpl.value, __tpl.set, None, 'TIPLOC')

    
    # Attribute act uses Python identifier act
    __act = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'act'), 'act', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPDT_act', _ImportedBinding__ct.ActivityType, unicode_default='  ')
    __act._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    __act._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 88, 2)
    
    act = property(__act.value, __act.set, None, 'Current Activity Codes')

    
    # Attribute planAct uses Python identifier planAct
    __planAct = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'planAct'), 'planAct', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPDT_planAct', _ImportedBinding__ct.ActivityType)
    __planAct._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    __planAct._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 93, 2)
    
    planAct = property(__planAct.value, __planAct.set, None, 'Planned Activity Codes (if different to current activities)')

    
    # Attribute can uses Python identifier can
    __can = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'can'), 'can', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPDT_can', pyxb.binding.datatypes.boolean, unicode_default='false')
    __can._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    __can._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 98, 2)
    
    can = property(__can.value, __can.set, None, 'Cancelled')

    
    # Attribute wta uses Python identifier wta
    __wta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wta'), 'wta', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPDT_wta', _ImportedBinding__ct.WTimeType, required=True)
    __wta._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 248, 2)
    __wta._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 248, 2)
    
    wta = property(__wta.value, __wta.set, None, 'Working Scheduled Time of Arrival')

    
    # Attribute wtd uses Python identifier wtd
    __wtd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wtd'), 'wtd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPDT_wtd', _ImportedBinding__ct.WTimeType)
    __wtd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 253, 2)
    __wtd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 253, 2)
    
    wtd = property(__wtd.value, __wtd.set, None, 'Working Scheduled Time of Departure')

    
    # Attribute rdelay uses Python identifier rdelay
    __rdelay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rdelay'), 'rdelay', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_OPDT_rdelay', _ImportedBinding__ct.DelayValueType, unicode_default='0')
    __rdelay._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 258, 2)
    __rdelay._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 258, 2)
    
    rdelay = property(__rdelay.value, __rdelay.set, None, "A delay value that is implied by a change to the service's route. This value has been added to the forecast lateness of the service at the previous schedule location when calculating the expected lateness of arrival at this location.")

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tpl.name() : __tpl,
        __act.name() : __act,
        __planAct.name() : __planAct,
        __can.name() : __can,
        __wta.name() : __wta,
        __wtd.name() : __wtd,
        __rdelay.name() : __rdelay
    })
_module_typeBindings.OPDT = OPDT
Namespace.addCategoryObject('typeBinding', 'OPDT', OPDT)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}Schedule with content type ELEMENT_ONLY
class Schedule (pyxb.binding.basis.complexTypeDefinition):
    """Train Schedule"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Schedule')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 264, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}OR uses Python identifier OR
    __OR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OR'), 'OR', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv2OR', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 270, 4), )

    
    OR = property(__OR.value, __OR.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}OPOR uses Python identifier OPOR
    __OPOR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OPOR'), 'OPOR', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv2OPOR', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 271, 4), )

    
    OPOR = property(__OPOR.value, __OPOR.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}IP uses Python identifier IP
    __IP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IP'), 'IP', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv2IP', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 272, 4), )

    
    IP = property(__IP.value, __IP.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}OPIP uses Python identifier OPIP
    __OPIP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OPIP'), 'OPIP', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv2OPIP', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 273, 4), )

    
    OPIP = property(__OPIP.value, __OPIP.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}PP uses Python identifier PP
    __PP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PP'), 'PP', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv2PP', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 274, 4), )

    
    PP = property(__PP.value, __PP.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}DT uses Python identifier DT
    __DT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DT'), 'DT', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv2DT', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 275, 4), )

    
    DT = property(__DT.value, __DT.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}OPDT uses Python identifier OPDT
    __OPDT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OPDT'), 'OPDT', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv2OPDT', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 276, 4), )

    
    OPDT = property(__OPDT.value, __OPDT.set, None, None)

    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}cancelReason uses Python identifier cancelReason
    __cancelReason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cancelReason'), 'cancelReason', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_httpwww_thalesgroup_comrttiPushPortSchedulesv2cancelReason', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 278, 3), )

    
    cancelReason = property(__cancelReason.value, __cancelReason.set, None, None)

    
    # Attribute rid uses Python identifier rid
    __rid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rid'), 'rid', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_rid', _ImportedBinding__ct.RIDType, required=True)
    __rid._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 280, 2)
    __rid._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 280, 2)
    
    rid = property(__rid.value, __rid.set, None, 'RTTI unique Train ID')

    
    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_uid', _ImportedBinding__ct.UIDType, required=True)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 285, 2)
    __uid._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 285, 2)
    
    uid = property(__uid.value, __uid.set, None, 'Train UID')

    
    # Attribute trainId uses Python identifier trainId
    __trainId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'trainId'), 'trainId', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_trainId', _ImportedBinding__ct.TrainIdType, required=True)
    __trainId._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 290, 2)
    __trainId._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 290, 2)
    
    trainId = property(__trainId.value, __trainId.set, None, 'Train ID (Headcode)')

    
    # Attribute rsid uses Python identifier rsid
    __rsid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rsid'), 'rsid', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_rsid', _ImportedBinding__ct2.RSIDType)
    __rsid._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 295, 2)
    __rsid._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 295, 2)
    
    rsid = property(__rsid.value, __rsid.set, None, 'Retail Service Identifier. Note that this may be either a full 8-character "portion identifier", or a base 6-character identifier, according to the available information provided to Darwin.')

    
    # Attribute ssd uses Python identifier ssd
    __ssd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ssd'), 'ssd', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_ssd', _ImportedBinding__ct.RTTIDateType, required=True)
    __ssd._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 300, 2)
    __ssd._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 300, 2)
    
    ssd = property(__ssd.value, __ssd.set, None, 'Scheduled Start Date')

    
    # Attribute toc uses Python identifier toc
    __toc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'toc'), 'toc', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_toc', _ImportedBinding__ct.TOCType, required=True)
    __toc._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 305, 2)
    __toc._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 305, 2)
    
    toc = property(__toc.value, __toc.set, None, 'ATOC Code')

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'status'), 'status', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_status', _ImportedBinding__ct.CIFTrainStatusType, unicode_default='P')
    __status._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 310, 2)
    __status._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 310, 2)
    
    status = property(__status.value, __status.set, None, 'Type of service, i.e. Train/Bus/Ship.')

    
    # Attribute trainCat uses Python identifier trainCat
    __trainCat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'trainCat'), 'trainCat', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_trainCat', _ImportedBinding__ct.CIFTrainCategoryType, unicode_default='OO')
    __trainCat._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 315, 2)
    __trainCat._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 315, 2)
    
    trainCat = property(__trainCat.value, __trainCat.set, None, 'Category of service.')

    
    # Attribute isPassengerSvc uses Python identifier isPassengerSvc
    __isPassengerSvc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isPassengerSvc'), 'isPassengerSvc', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_isPassengerSvc', pyxb.binding.datatypes.boolean, unicode_default='true')
    __isPassengerSvc._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 320, 2)
    __isPassengerSvc._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 320, 2)
    
    isPassengerSvc = property(__isPassengerSvc.value, __isPassengerSvc.set, None, 'True if Darwin classifies the train category as a passenger service.')

    
    # Attribute isActive uses Python identifier isActive
    __isActive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isActive'), 'isActive', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_isActive', pyxb.binding.datatypes.boolean, unicode_default='true')
    __isActive._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 325, 2)
    __isActive._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 325, 2)
    
    isActive = property(__isActive.value, __isActive.set, None, 'Indicates if this service is active in Darwin. Note that schedules should be assumed to be inactive until a message is received to indicate otherwise.')

    
    # Attribute deleted uses Python identifier deleted
    __deleted = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'deleted'), 'deleted', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_deleted', pyxb.binding.datatypes.boolean, unicode_default='false')
    __deleted._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 330, 2)
    __deleted._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 330, 2)
    
    deleted = property(__deleted.value, __deleted.set, None, 'Service has been deleted and should not be used/displayed.')

    
    # Attribute isCharter uses Python identifier isCharter
    __isCharter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isCharter'), 'isCharter', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_Schedule_isCharter', pyxb.binding.datatypes.boolean, unicode_default='false')
    __isCharter._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 335, 2)
    __isCharter._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 335, 2)
    
    isCharter = property(__isCharter.value, __isCharter.set, None, 'Indicates if this service is a charter service.')

    _ElementMap.update({
        __OR.name() : __OR,
        __OPOR.name() : __OPOR,
        __IP.name() : __IP,
        __OPIP.name() : __OPIP,
        __PP.name() : __PP,
        __DT.name() : __DT,
        __OPDT.name() : __OPDT,
        __cancelReason.name() : __cancelReason
    })
    _AttributeMap.update({
        __rid.name() : __rid,
        __uid.name() : __uid,
        __trainId.name() : __trainId,
        __rsid.name() : __rsid,
        __ssd.name() : __ssd,
        __toc.name() : __toc,
        __status.name() : __status,
        __trainCat.name() : __trainCat,
        __isPassengerSvc.name() : __isPassengerSvc,
        __isActive.name() : __isActive,
        __deleted.name() : __deleted,
        __isCharter.name() : __isCharter
    })
_module_typeBindings.Schedule = Schedule
Namespace.addCategoryObject('typeBinding', 'Schedule', Schedule)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Schedules/v2}DeactivatedSchedule with content type EMPTY
class DeactivatedSchedule (pyxb.binding.basis.complexTypeDefinition):
    """Notification that a Train Schedule is now deactivated in Darwin."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DeactivatedSchedule')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 341, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute rid uses Python identifier rid
    __rid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rid'), 'rid', '__httpwww_thalesgroup_comrttiPushPortSchedulesv2_DeactivatedSchedule_rid', _ImportedBinding__ct.RIDType, required=True)
    __rid._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 345, 2)
    __rid._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 345, 2)
    
    rid = property(__rid.value, __rid.set, None, 'RTTI unique Train ID')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __rid.name() : __rid
    })
_module_typeBindings.DeactivatedSchedule = DeactivatedSchedule
Namespace.addCategoryObject('typeBinding', 'DeactivatedSchedule', DeactivatedSchedule)




Association._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'main'), AssocService, scope=Association, documentation='The through, previous working or link-to service', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 47, 3)))

Association._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'assoc'), AssocService, scope=Association, documentation='The starting, terminating, subsequent working or link-from service', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 52, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Association._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'main')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 47, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Association._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'assoc')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 52, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Association._Automaton = _BuildAutomaton()




Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OR'), OR, scope=Schedule, location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 270, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OPOR'), OPOR, scope=Schedule, location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 271, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IP'), IP, scope=Schedule, location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 272, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OPIP'), OPIP, scope=Schedule, location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 273, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PP'), PP, scope=Schedule, location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 274, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DT'), DT, scope=Schedule, location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 275, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OPDT'), OPDT, scope=Schedule, location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 276, 4)))

Schedule._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cancelReason'), _ImportedBinding__ct.DisruptionReasonType, scope=Schedule, location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 278, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=2, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 269, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 278, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OR')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 270, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OPOR')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 271, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IP')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 272, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OPIP')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 273, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PP')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 274, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DT')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 275, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OPDT')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 276, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Schedule._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cancelReason')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTSchedules_v2.xsd', 278, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Schedule._Automaton = _BuildAutomaton_()

