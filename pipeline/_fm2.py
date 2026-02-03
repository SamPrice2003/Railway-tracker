# ./_fm2.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c2e233e3b07de662af67ce6b6adb735f452d8b4a
# Generated 2026-02-02 18:03:54.409485 by PyXB version 1.2.6 using Python 3.14.0.final.0
# Namespace http://www.thalesgroup.com/rtti/PushPort/Formations/v2 [xmlns:fm2]

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
import _ct3 as _ImportedBinding__ct3
import _ct4 as _ImportedBinding__ct4
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.thalesgroup.com/rtti/PushPort/Formations/v2', create_if_missing=True)
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


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Formations/v2}CoachList with content type ELEMENT_ONLY
class CoachList (pyxb.binding.basis.complexTypeDefinition):
    """A list of coach data for a formation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CoachList')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 64, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Formations/v2}coach uses Python identifier coach
    __coach = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coach'), 'coach', '__httpwww_thalesgroup_comrttiPushPortFormationsv2_CoachList_httpwww_thalesgroup_comrttiPushPortFormationsv2coach', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 69, 3), )

    
    coach = property(__coach.value, __coach.set, None, 'An individual coach in a formation.')

    _ElementMap.update({
        __coach.name() : __coach
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CoachList = CoachList
Namespace.addCategoryObject('typeBinding', 'CoachList', CoachList)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Formations/v2}ScheduleFormations with content type ELEMENT_ONLY
class ScheduleFormations (pyxb.binding.basis.complexTypeDefinition):
    """Type describing all of the Train Formations set for a Schedule."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ScheduleFormations')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 20, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Formations/v2}formation uses Python identifier formation
    __formation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'formation'), 'formation', '__httpwww_thalesgroup_comrttiPushPortFormationsv2_ScheduleFormations_httpwww_thalesgroup_comrttiPushPortFormationsv2formation', True, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 25, 3), )

    
    formation = property(__formation.value, __formation.set, None, 'An individual formation for all or part of the service.')

    
    # Attribute rid uses Python identifier rid
    __rid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rid'), 'rid', '__httpwww_thalesgroup_comrttiPushPortFormationsv2_ScheduleFormations_rid', _ImportedBinding__ct.RIDType, required=True)
    __rid._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 31, 2)
    __rid._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 31, 2)
    
    rid = property(__rid.value, __rid.set, None, 'RTTI unique Train Identifier')

    _ElementMap.update({
        __formation.name() : __formation
    })
    _AttributeMap.update({
        __rid.name() : __rid
    })
_module_typeBindings.ScheduleFormations = ScheduleFormations
Namespace.addCategoryObject('typeBinding', 'ScheduleFormations', ScheduleFormations)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Formations/v2}Formation with content type ELEMENT_ONLY
class Formation (pyxb.binding.basis.complexTypeDefinition):
    """Type describing a Train Formation for a Schedule."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Formation')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 37, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Formations/v2}coaches uses Python identifier coaches
    __coaches = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'coaches'), 'coaches', '__httpwww_thalesgroup_comrttiPushPortFormationsv2_Formation_httpwww_thalesgroup_comrttiPushPortFormationsv2coaches', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 42, 3), )

    
    coaches = property(__coaches.value, __coaches.set, None, 'A list of coaches in this formation.')

    
    # Attribute fid uses Python identifier fid
    __fid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fid'), 'fid', '__httpwww_thalesgroup_comrttiPushPortFormationsv2_Formation_fid', _ImportedBinding__ct3.FormationIDType, required=True)
    __fid._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 48, 2)
    __fid._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 48, 2)
    
    fid = property(__fid.value, __fid.set, None, 'The unique identifier of this formation data.')

    
    # Attribute src uses Python identifier src
    __src = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'src'), 'src', '__httpwww_thalesgroup_comrttiPushPortFormationsv2_Formation_src', pyxb.binding.datatypes.string)
    __src._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 53, 2)
    __src._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 53, 2)
    
    src = property(__src.value, __src.set, None, 'The source of the formation data.')

    
    # Attribute srcInst uses Python identifier srcInst
    __srcInst = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'srcInst'), 'srcInst', '__httpwww_thalesgroup_comrttiPushPortFormationsv2_Formation_srcInst', _ImportedBinding__ct.SourceTypeInst)
    __srcInst._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 58, 2)
    __srcInst._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 58, 2)
    
    srcInst = property(__srcInst.value, __srcInst.set, None, 'The RTTI instance ID of the src (if any).')

    _ElementMap.update({
        __coaches.name() : __coaches
    })
    _AttributeMap.update({
        __fid.name() : __fid,
        __src.name() : __src,
        __srcInst.name() : __srcInst
    })
_module_typeBindings.Formation = Formation
Namespace.addCategoryObject('typeBinding', 'Formation', Formation)


# Complex type {http://www.thalesgroup.com/rtti/PushPort/Formations/v2}CoachData with content type ELEMENT_ONLY
class CoachData (pyxb.binding.basis.complexTypeDefinition):
    """Data for an individual coach in a formation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CoachData')
    _XSDLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 76, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.thalesgroup.com/rtti/PushPort/Formations/v2}toilet uses Python identifier toilet
    __toilet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'toilet'), 'toilet', '__httpwww_thalesgroup_comrttiPushPortFormationsv2_CoachData_httpwww_thalesgroup_comrttiPushPortFormationsv2toilet', False, pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 81, 3), )

    
    toilet = property(__toilet.value, __toilet.set, None, 'The availability of a toilet in this coach. E.g. "Unknown", "None" , "Standard" or "Accessible". Note that other values may be supplied in the future without a schema change. If no toilet availability is supplied then it should be assumed to be "Unknown".')

    
    # Attribute coachNumber uses Python identifier coachNumber
    __coachNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coachNumber'), 'coachNumber', '__httpwww_thalesgroup_comrttiPushPortFormationsv2_CoachData_coachNumber', _ImportedBinding__ct3.CoachNumberType, required=True)
    __coachNumber._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 87, 2)
    __coachNumber._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 87, 2)
    
    coachNumber = property(__coachNumber.value, __coachNumber.set, None, 'The number/identifier for this coach, e.g. "A".')

    
    # Attribute coachClass uses Python identifier coachClass
    __coachClass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'coachClass'), 'coachClass', '__httpwww_thalesgroup_comrttiPushPortFormationsv2_CoachData_coachClass', _ImportedBinding__ct3.CoachClassType)
    __coachClass._DeclarationLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 92, 2)
    __coachClass._UseLocation = pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 92, 2)
    
    coachClass = property(__coachClass.value, __coachClass.set, None, 'The class of the coach, e.g. "First" or "Standard".')

    _ElementMap.update({
        __toilet.name() : __toilet
    })
    _AttributeMap.update({
        __coachNumber.name() : __coachNumber,
        __coachClass.name() : __coachClass
    })
_module_typeBindings.CoachData = CoachData
Namespace.addCategoryObject('typeBinding', 'CoachData', CoachData)




CoachList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coach'), CoachData, scope=CoachList, documentation='An individual coach in a formation.', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 69, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CoachList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coach')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 69, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CoachList._Automaton = _BuildAutomaton()




ScheduleFormations._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'formation'), Formation, scope=ScheduleFormations, documentation='An individual formation for all or part of the service.', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 25, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 25, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ScheduleFormations._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'formation')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 25, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ScheduleFormations._Automaton = _BuildAutomaton_()




Formation._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'coaches'), CoachList, scope=Formation, documentation='A list of coaches in this formation.', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 42, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Formation._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'coaches')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 42, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Formation._Automaton = _BuildAutomaton_2()




CoachData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'toilet'), _ImportedBinding__ct4.ToiletAvailabilityType, scope=CoachData, documentation='The availability of a toilet in this coach. E.g. "Unknown", "None" , "Standard" or "Accessible". Note that other values may be supplied in the future without a schema change. If no toilet availability is supplied then it should be assumed to be "Unknown".', location=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 81, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 81, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CoachData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'toilet')), pyxb.utils.utility.Location('/Users/omaryahya/Sigma-Labs/Week_14/railway-tracker/pipeline/ppv16/rttiPPTFormations_v2.xsd', 81, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CoachData._Automaton = _BuildAutomaton_3()

