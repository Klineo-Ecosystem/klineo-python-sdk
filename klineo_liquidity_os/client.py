# Generated from openapi/liquidity-operating-system-v2.openapi.json. Do not edit.
from __future__ import annotations

from dataclasses import dataclass, field
from .runtime import LiquidityOsApiError, LiquidityOsResponseError, LiquidityOsTransport, LiquidityOsTransportError, ResponseObserver
from typing import Literal, NotRequired, Optional, TypeAlias, TypedDict, Union, cast

AtomicAmount: TypeAlias = str

PositiveAtomicAmount: TypeAlias = str

SignedAtomicAmount: TypeAlias = str

Hash: TypeAlias = str

Address: TypeAlias = str

Pips: TypeAlias = int

OperatingSystemRecordStatus: TypeAlias = Literal["DRAFT", "VALIDATED", "ACTIVE", "PAUSED", "COMPLETED", "EXPIRED", "REVOKED", "SUPERSEDED", "UNAVAILABLE"]

OperatingSystemRecordType: TypeAlias = Literal["ISSUER_INTENT", "SIMULATION_STUDY", "SIMULATION_SHARE", "STRATEGY_DEFINITION", "PROPOSAL_WORKSPACE", "LAUNCH_PLAN", "UNLOCK_IMPACT", "MARKET_QUALITY_SCORE", "EXECUTION_ATTRIBUTION", "ANOMALY", "TREASURY_LEDGER_ENTRY", "CAPITAL_REQUIREMENT_STUDY", "TREASURY_STRESS_TEST", "VENUE_PROFILE", "VENUE_OBSERVATION", "ALLOCATION_PLAN", "MIGRATION_PLAN", "AUTONOMY_POLICY", "POLICY_INTENT_DRAFT", "PROTECTED_EXECUTION_QUOTE_SET", "PROTECTED_EXECUTION_PLAN", "DEVELOPER_CREDENTIAL", "WEBHOOK_SUBSCRIPTION", "STRATEGY_PACKAGE", "PARTNER_TENANT", "PARTNER_CONSENT", "MARKET_MAKER_MANDATE", "INCENTIVE_PROGRAM", "LIQUIDITY_PASSPORT"]

class RecordEnvelope(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: dict[str, object]
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class IssuerIntentDurationVariant1(TypedDict):
    kind: Literal["UNTIL"]
    endsAt: str

class IssuerIntentDurationVariant2(TypedDict):
    kind: Literal["ROLLING"]
    days: int

IssuerIntentDuration: TypeAlias = Union[IssuerIntentDurationVariant1, IssuerIntentDurationVariant2]

class IssuerIntent(TypedDict):
    name: str
    vaultId: NotRequired[str]
    quoteSymbol: str
    targetTradeSizeQuote: PositiveAtomicAmount
    maximumSlippagePips: int
    executableDepthQuote: PositiveAtomicAmount
    executableDepthBandPips: int
    treasuryReservePips: Pips
    minimumPriceX18: NotRequired[AtomicAmount]
    capitalCeilingQuote: PositiveAtomicAmount
    maximumDailyTurnoverPips: Pips
    acceptableVolatilityPips: Pips
    duration: IssuerIntentDuration
    prohibitedBehaviors: list[str]

class LiquidityPlan(TypedDict):
    kind: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    requiredCapitalQuote: AtomicAmount
    deployableCapitalQuote: AtomicAmount
    stableReserveQuote: AtomicAmount
    emergencyReserveQuote: AtomicAmount
    rangeWidthPips: Pips
    expectedSlippagePips: Pips
    expectedFeeIncomeLowQuote: AtomicAmount
    expectedFeeIncomeHighQuote: AtomicAmount
    inventoryExposurePips: Pips
    maximumDailyTurnoverPips: Pips
    satisfiesIntent: bool
    reasons: list[str]

class LiquidityPlanVariant(TypedDict):
    kind: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    requiredCapitalQuote: AtomicAmount
    deployableCapitalQuote: AtomicAmount
    stableReserveQuote: AtomicAmount
    emergencyReserveQuote: AtomicAmount
    rangeWidthPips: Pips
    expectedSlippagePips: Pips
    expectedFeeIncomeLowQuote: AtomicAmount
    expectedFeeIncomeHighQuote: AtomicAmount
    inventoryExposurePips: Pips
    maximumDailyTurnoverPips: Pips
    satisfiesIntent: bool
    reasons: list[str]

class CapitalRequirementStudy(TypedDict):
    calculationVersion: Literal["capital-requirement-v1", "capital-requirement-v2"]
    intent: IssuerIntent
    minimumCapitalQuote: AtomicAmount
    recommendedRangeWidthPips: Pips
    requiredStableReserveQuote: AtomicAmount
    expectedFeeIncomeLowQuote: AtomicAmount
    expectedFeeIncomeHighQuote: AtomicAmount
    inventoryExposurePips: Pips
    confidencePips: Pips
    variants: list[LiquidityPlanVariant]
    assumptions: list[str]

class UnlockTranche(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: PositiveAtomicAmount
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: Pips
    confidencePips: Pips
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[Hash]

class UnlockImpactSourceObservation(TypedDict):
    schemaVersion: Literal["unlock-impact-source-observation-v1"]
    observationId: str
    chainId: int
    venueId: str
    assetMappingId: str
    tokenPriceX18: PositiveAtomicAmount
    tokenDecimals: int
    quoteDecimals: int
    currentUsableDepthQuote: PositiveAtomicAmount
    currentStableReserveQuote: AtomicAmount
    observedAt: str
    providerId: str
    providerResourceVersion: Hash
    providerAttestationHash: Hash
    payloadHash: Hash
    signature: str

class UnlockImpactCorrelationGroupsItemSellPressureTokenRange(TypedDict):
    p5: AtomicAmount
    p50: AtomicAmount
    p95: AtomicAmount

class UnlockImpactCorrelationGroupsItem(TypedDict):
    groupId: str
    unlockIds: list[str]
    totalUnlockedToken: AtomicAmount
    confidencePips: Pips
    sellPressureTokenRange: UnlockImpactCorrelationGroupsItemSellPressureTokenRange

class UnlockImpactSellPressureTokenRange(TypedDict):
    p5: AtomicAmount
    p50: AtomicAmount
    p95: AtomicAmount

class UnlockImpactSellPressureQuoteRange(TypedDict):
    p5: AtomicAmount
    p50: AtomicAmount
    p95: AtomicAmount

class UnlockImpactPriceImpactPipsRange(TypedDict):
    p5: Pips
    p50: Pips
    p95: Pips

class UnlockImpact(TypedDict):
    calculationVersion: Literal["unlock-impact-v1", "unlock-impact-v2"]
    unlockIds: list[str]
    sourceLaunchPlanId: NotRequired[str]
    sourceObservation: NotRequired[UnlockImpactSourceObservation]
    inputHash: NotRequired[Hash]
    inputSnapshot: NotRequired[UnlockImpactInputSnapshot]
    correlationGroups: NotRequired[list[UnlockImpactCorrelationGroupsItem]]
    sellPressureTokenRange: NotRequired[UnlockImpactSellPressureTokenRange]
    sellPressureQuoteRange: NotRequired[UnlockImpactSellPressureQuoteRange]
    priceImpactPipsRange: NotRequired[UnlockImpactPriceImpactPipsRange]
    expectedSellPressureToken: AtomicAmount
    expectedSellPressureQuote: AtomicAmount
    usableDepthAfterQuote: AtomicAmount
    expectedPriceImpactPips: Pips
    requiredStableReserveQuote: AtomicAmount
    recommendedRangeShiftPips: int
    treasuryRiskPips: Pips
    confidencePips: Pips
    warnings: list[str]

class ScenarioDefinition(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: Pips
    liquidityWithdrawalPips: Pips
    oneSidedFlowPips: Pips
    gasIncreasePips: Pips
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[Pips]
    platformFeePips: NotRequired[Pips]
    unlocks: list[UnlockTranche]

class DistributionPercentiles(TypedDict):
    p5: SignedAtomicAmount
    p25: SignedAtomicAmount
    p50: SignedAtomicAmount
    p75: SignedAtomicAmount
    p95: SignedAtomicAmount

class PipsPercentiles(TypedDict):
    p5: Pips
    p25: Pips
    p50: Pips
    p75: Pips
    p95: Pips

class SimulationStudySourceLineage(TypedDict):
    schemaVersion: Literal["simulation-study-source-lineage-v1"]
    sourceKind: Literal["ISSUER_INTENT", "LAUNCH_PLAN", "SANDBOX"]
    publicationEligibility: Literal["ELIGIBLE", "INELIGIBLE_UNBOUND", "INELIGIBLE_SANDBOX"]
    vaultId: NotRequired[str]
    issuerIntentId: NotRequired[str]
    issuerIntentVersion: NotRequired[int]
    issuerIntentResourceVersion: NotRequired[Hash]
    issuerIntentArtifactHash: NotRequired[Hash]
    studyInputHash: Hash
    publicationAdmissionHash: Hash

class SimulationStudyInputSnapshot(TypedDict):
    schemaVersion: Literal["simulation-study-input-snapshot-v1"]
    engineVersion: Literal["digital-twin-pcg64-fixed-v2"]
    seed: str
    pathCount: Literal[2000, 10000]
    stepCount: int
    targetTradeSizeQuote: PositiveAtomicAmount
    startingPortfolioQuote: PositiveAtomicAmount
    startingDepthQuote: PositiveAtomicAmount
    startingInventoryPips: Pips
    scenario: ScenarioDefinition
    variants: list[LiquidityPlanVariant]

class DisclosedSimulationStudyInputSnapshotScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: Pips
    liquidityWithdrawalPips: Pips
    oneSidedFlowPips: Pips
    gasIncreasePips: Pips
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[Pips]
    platformFeePips: NotRequired[Pips]
    unlocks: NotRequired[list[UnlockTranche]]

class DisclosedSimulationStudyInputSnapshot(TypedDict):
    schemaVersion: Literal["simulation-study-input-snapshot-v1"]
    engineVersion: Literal["digital-twin-pcg64-fixed-v2"]
    seed: str
    pathCount: Literal[2000, 10000]
    stepCount: int
    targetTradeSizeQuote: PositiveAtomicAmount
    startingPortfolioQuote: PositiveAtomicAmount
    startingDepthQuote: PositiveAtomicAmount
    startingInventoryPips: Pips
    scenario: DisclosedSimulationStudyInputSnapshotScenario
    variants: list[LiquidityPlanVariant]

class DisclosedSimulationStudyVariant1Scenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: Pips
    liquidityWithdrawalPips: Pips
    oneSidedFlowPips: Pips
    gasIncreasePips: Pips
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[Pips]
    platformFeePips: NotRequired[Pips]
    unlocks: NotRequired[list[UnlockTranche]]

class DisclosedSimulationStudyVariant1VariantsItemDriversItem(TypedDict):
    driver: Literal["PRICE_PATH", "VOLATILITY", "FLOW", "LIQUIDITY", "UNLOCK", "GAS", "RESERVE"]
    impactQuote: SignedAtomicAmount
    evidence: str
    method: Literal["DETERMINISTIC_COUNTERFACTUAL_DELTA_V1"]

class DisclosedSimulationStudyVariant1VariantsItem(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    endingValueQuote: DistributionPercentiles
    slippagePips: PipsPercentiles
    drawdownPips: PipsPercentiles
    turnoverQuote: DistributionPercentiles
    gasCostQuote: DistributionPercentiles
    feeIncomeQuote: DistributionPercentiles
    protocolFeesQuote: DistributionPercentiles
    platformFeesQuote: DistributionPercentiles
    inventoryPips: PipsPercentiles
    minimumDepthQuote: DistributionPercentiles
    reserveBreachProbabilityPips: Pips
    drivers: NotRequired[list[DisclosedSimulationStudyVariant1VariantsItemDriversItem]]

class DisclosedSimulationStudyVariant1Treasury(TypedDict):
    unlocks: list[UnlockTranche]

class DisclosedSimulationStudyVariant1Policy(TypedDict):
    availability: Literal["NOT_ATTACHED_TO_STUDY"]

class DisclosedSimulationStudyVariant1DisclosureApplied(TypedDict):
    drivers: bool
    treasury: bool
    policy: bool

class DisclosedSimulationStudyVariant1(TypedDict):
    engineVersion: Literal["digital-twin-pcg64-fixed-v1"]
    seed: str
    pathCount: Literal[2000, 10000]
    stepCount: int
    scenario: DisclosedSimulationStudyVariant1Scenario
    variants: list[DisclosedSimulationStudyVariant1VariantsItem]
    recommendedVariant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    warnings: list[str]
    replayCompleteness: Literal["HISTORICAL_V1_INPUT_SNAPSHOT_UNAVAILABLE"]
    inputHash: Union[Hash, None]
    sourceLineage: NotRequired[SimulationStudySourceLineage]
    treasury: NotRequired[DisclosedSimulationStudyVariant1Treasury]
    policy: NotRequired[DisclosedSimulationStudyVariant1Policy]
    disclosureApplied: DisclosedSimulationStudyVariant1DisclosureApplied

class DisclosedSimulationStudyVariant2Scenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: Pips
    liquidityWithdrawalPips: Pips
    oneSidedFlowPips: Pips
    gasIncreasePips: Pips
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[Pips]
    platformFeePips: NotRequired[Pips]
    unlocks: NotRequired[list[UnlockTranche]]

class DisclosedSimulationStudyVariant2VariantsItemDriversItem(TypedDict):
    driver: Literal["PRICE_PATH", "VOLATILITY", "FLOW", "LIQUIDITY", "UNLOCK", "GAS", "RESERVE"]
    impactQuote: SignedAtomicAmount
    evidence: str
    method: Literal["DETERMINISTIC_COUNTERFACTUAL_DELTA_V1"]

class DisclosedSimulationStudyVariant2VariantsItem(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    endingValueQuote: DistributionPercentiles
    slippagePips: PipsPercentiles
    drawdownPips: PipsPercentiles
    turnoverQuote: DistributionPercentiles
    gasCostQuote: DistributionPercentiles
    feeIncomeQuote: DistributionPercentiles
    protocolFeesQuote: DistributionPercentiles
    platformFeesQuote: DistributionPercentiles
    inventoryPips: PipsPercentiles
    minimumDepthQuote: DistributionPercentiles
    reserveBreachProbabilityPips: Pips
    drivers: NotRequired[list[DisclosedSimulationStudyVariant2VariantsItemDriversItem]]

class DisclosedSimulationStudyVariant2Treasury(TypedDict):
    unlocks: list[UnlockTranche]

class DisclosedSimulationStudyVariant2Policy(TypedDict):
    availability: Literal["NOT_ATTACHED_TO_STUDY"]

class DisclosedSimulationStudyVariant2DisclosureApplied(TypedDict):
    drivers: bool
    treasury: bool
    policy: bool

class DisclosedSimulationStudyVariant2(TypedDict):
    engineVersion: Literal["digital-twin-pcg64-fixed-v2"]
    seed: str
    pathCount: Literal[2000, 10000]
    stepCount: int
    scenario: DisclosedSimulationStudyVariant2Scenario
    variants: list[DisclosedSimulationStudyVariant2VariantsItem]
    recommendedVariant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    warnings: list[str]
    replayCompleteness: Literal["COMPLETE_INPUT_SNAPSHOT"]
    inputHash: Hash
    inputSnapshot: DisclosedSimulationStudyInputSnapshot
    sourceLineage: SimulationStudySourceLineage
    treasury: NotRequired[DisclosedSimulationStudyVariant2Treasury]
    policy: NotRequired[DisclosedSimulationStudyVariant2Policy]
    disclosureApplied: DisclosedSimulationStudyVariant2DisclosureApplied

DisclosedSimulationStudy: TypeAlias = Union[DisclosedSimulationStudyVariant1, DisclosedSimulationStudyVariant2]

class SimulationStudyVariant1VariantsItemDriversItem(TypedDict):
    driver: Literal["PRICE_PATH", "VOLATILITY", "FLOW", "LIQUIDITY", "UNLOCK", "GAS", "RESERVE"]
    impactQuote: SignedAtomicAmount
    evidence: str
    method: Literal["DETERMINISTIC_COUNTERFACTUAL_DELTA_V1"]

class SimulationStudyVariant1VariantsItem(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    endingValueQuote: DistributionPercentiles
    slippagePips: PipsPercentiles
    drawdownPips: PipsPercentiles
    turnoverQuote: DistributionPercentiles
    gasCostQuote: DistributionPercentiles
    feeIncomeQuote: DistributionPercentiles
    protocolFeesQuote: DistributionPercentiles
    platformFeesQuote: DistributionPercentiles
    inventoryPips: PipsPercentiles
    minimumDepthQuote: DistributionPercentiles
    reserveBreachProbabilityPips: Pips
    drivers: list[SimulationStudyVariant1VariantsItemDriversItem]

class SimulationStudyVariant1(TypedDict):
    engineVersion: Literal["digital-twin-pcg64-fixed-v1"]
    seed: str
    pathCount: Literal[2000, 10000]
    stepCount: int
    scenario: ScenarioDefinition
    variants: list[SimulationStudyVariant1VariantsItem]
    recommendedVariant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    warnings: list[str]
    sourceLineage: NotRequired[SimulationStudySourceLineage]

class SimulationStudyVariant2VariantsItemDriversItem(TypedDict):
    driver: Literal["PRICE_PATH", "VOLATILITY", "FLOW", "LIQUIDITY", "UNLOCK", "GAS", "RESERVE"]
    impactQuote: SignedAtomicAmount
    evidence: str
    method: Literal["DETERMINISTIC_COUNTERFACTUAL_DELTA_V1"]

class SimulationStudyVariant2VariantsItem(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    endingValueQuote: DistributionPercentiles
    slippagePips: PipsPercentiles
    drawdownPips: PipsPercentiles
    turnoverQuote: DistributionPercentiles
    gasCostQuote: DistributionPercentiles
    feeIncomeQuote: DistributionPercentiles
    protocolFeesQuote: DistributionPercentiles
    platformFeesQuote: DistributionPercentiles
    inventoryPips: PipsPercentiles
    minimumDepthQuote: DistributionPercentiles
    reserveBreachProbabilityPips: Pips
    drivers: list[SimulationStudyVariant2VariantsItemDriversItem]

class SimulationStudyVariant2(TypedDict):
    engineVersion: Literal["digital-twin-pcg64-fixed-v2"]
    seed: str
    pathCount: Literal[2000, 10000]
    stepCount: int
    scenario: ScenarioDefinition
    variants: list[SimulationStudyVariant2VariantsItem]
    recommendedVariant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    warnings: list[str]
    inputSnapshot: SimulationStudyInputSnapshot
    sourceLineage: SimulationStudySourceLineage

class SimulationStudyVariant3(TypedDict):
    engineVersion: Literal["digital-twin-pcg64-fixed-v2"]
    seed: str
    pathCount: Literal[10000]
    stepCount: int
    scenario: ScenarioDefinition
    variants: list[object]
    recommendedVariant: None
    warnings: list[str]
    state: Literal["QUEUED"]
    inputHash: Hash
    inputSnapshot: SimulationStudyInputSnapshot
    sourceLineage: SimulationStudySourceLineage

SimulationStudy: TypeAlias = Union[SimulationStudyVariant1, SimulationStudyVariant2, SimulationStudyVariant3]

class StrategyPackageSafetyEnvelope(TypedDict):
    supportedAssetIds: list[str]
    supportedVenueIds: list[str]
    maximumCapitalQuote: AtomicAmount
    riskClass: Literal["LOW", "MODERATE", "HIGH", "EXPERIMENTAL"]
    failureConditions: list[str]
    safetyEnvelopeHash: Hash

class StrategyPackageSourceLineage(TypedDict):
    schemaVersion: Literal["strategy-package-source-lineage-v1"]
    sourcePackageId: str
    sourcePackageVersion: int
    sourcePackageResourceVersion: Hash
    sourcePackageArtifactHash: Hash
    sourcePackageSemanticVersion: str
    sourcePackageContentHash: Hash
    compilerHash: Hash
    approvalRegistryEvidenceHash: Hash
    supportedAssetIds: list[str]
    supportedVenueIds: list[str]
    maximumCapitalQuote: AtomicAmount
    riskClass: Literal["LOW", "MODERATE", "HIGH", "EXPERIMENTAL"]
    failureConditions: list[str]
    safetyEnvelopeHash: Hash

class StrategyDefinitionV2InputSleevesItem(TypedDict):
    id: str
    kind: Literal["CORE_LIQUIDITY", "DEFENSIVE_DOWNSIDE", "UPSIDE_SELLING", "STABLE_RESERVE", "EMERGENCY_RESERVE"]
    allocationPips: Pips
    lowerPriceOffsetPips: int
    upperPriceOffsetPips: int
    minimumCapitalQuote: AtomicAmount
    maximumCapitalQuote: AtomicAmount
    enabled: bool

class StrategyDefinitionV2InputTriggersItem(TypedDict):
    id: str
    metric: Literal["PRICE", "INVENTORY", "DEPTH", "VOLATILITY", "ORACLE_HEALTH", "TIME"]
    operator: Literal["LT", "LTE", "GT", "GTE", "EQ"]
    threshold: str
    response: Literal["RECOMMEND", "PREPARE", "TIGHTEN", "PAUSE"]

class StrategyDefinitionV2Input(TypedDict):
    name: str
    family: Literal["BOOTSTRAP", "MAINTAIN", "DIVERSIFY", "COMPOSED"]
    compilerVersion: Literal["strategy-dsl-v1"]
    sleeves: list[StrategyDefinitionV2InputSleevesItem]
    triggers: list[StrategyDefinitionV2InputTriggersItem]
    cooldownSeconds: int
    maximumDailyTurnoverPips: Pips
    minimumPriceX18: NotRequired[AtomicAmount]
    capitalLimitQuote: AtomicAmount
    oracleMaximumAgeSeconds: int
    worstCaseLossLimitPips: Pips
    legacyStrategyVersion: NotRequired[str]

class StrategyDefinitionV2SleevesItem(TypedDict):
    id: str
    kind: Literal["CORE_LIQUIDITY", "DEFENSIVE_DOWNSIDE", "UPSIDE_SELLING", "STABLE_RESERVE", "EMERGENCY_RESERVE"]
    allocationPips: Pips
    lowerPriceOffsetPips: int
    upperPriceOffsetPips: int
    minimumCapitalQuote: AtomicAmount
    maximumCapitalQuote: AtomicAmount
    enabled: bool

class StrategyDefinitionV2TriggersItem(TypedDict):
    id: str
    metric: Literal["PRICE", "INVENTORY", "DEPTH", "VOLATILITY", "ORACLE_HEALTH", "TIME"]
    operator: Literal["LT", "LTE", "GT", "GTE", "EQ"]
    threshold: str
    response: Literal["RECOMMEND", "PREPARE", "TIGHTEN", "PAUSE"]

class StrategyDefinitionV2(TypedDict):
    name: str
    family: Literal["BOOTSTRAP", "MAINTAIN", "DIVERSIFY", "COMPOSED"]
    compilerVersion: Literal["strategy-dsl-v1"]
    sleeves: list[StrategyDefinitionV2SleevesItem]
    triggers: list[StrategyDefinitionV2TriggersItem]
    cooldownSeconds: int
    maximumDailyTurnoverPips: Pips
    minimumPriceX18: NotRequired[AtomicAmount]
    capitalLimitQuote: AtomicAmount
    oracleMaximumAgeSeconds: int
    worstCaseLossLimitPips: Pips
    legacyStrategyVersion: NotRequired[str]
    sourcePackage: NotRequired[StrategyPackageSourceLineage]

class StrategyProposalAdmissionOracleObservation(TypedDict):
    observedAt: str
    payloadHash: Hash
    signature: str

class StrategyProposalAdmissionChecksALLOCATION(TypedDict):
    passed: bool
    evidence: str

class StrategyProposalAdmissionChecksRANGE(TypedDict):
    passed: bool
    evidence: str

class StrategyProposalAdmissionChecksLIQUIDITY(TypedDict):
    passed: bool
    evidence: str

class StrategyProposalAdmissionChecksRESERVE(TypedDict):
    passed: bool
    evidence: str

class StrategyProposalAdmissionChecksORACLE(TypedDict):
    passed: bool
    evidence: str

class StrategyProposalAdmissionChecksPOLICY(TypedDict):
    passed: bool
    evidence: str

class StrategyProposalAdmissionChecksWORSTCASE(TypedDict):
    passed: bool
    evidence: str

class StrategyProposalAdmissionChecksCOMPLETEDSIMULATION(TypedDict):
    passed: bool
    evidence: str

class StrategyProposalAdmissionChecks(TypedDict):
    ALLOCATION: StrategyProposalAdmissionChecksALLOCATION
    RANGE: StrategyProposalAdmissionChecksRANGE
    LIQUIDITY: StrategyProposalAdmissionChecksLIQUIDITY
    RESERVE: StrategyProposalAdmissionChecksRESERVE
    ORACLE: StrategyProposalAdmissionChecksORACLE
    POLICY: StrategyProposalAdmissionChecksPOLICY
    WORST_CASE: StrategyProposalAdmissionChecksWORSTCASE
    COMPLETED_SIMULATION: StrategyProposalAdmissionChecksCOMPLETEDSIMULATION

class StrategyProposalAdmission(TypedDict):
    admissionVersion: Literal["strategy-proposal-admission-v1"]
    strategyDefinitionId: str
    strategyDefinitionVersion: int
    strategyDefinitionResourceVersion: Hash
    strategyDefinitionArtifactHash: Hash
    issuerIntentId: str
    issuerIntentVersion: int
    issuerIntentResourceVersion: Hash
    issuerIntentArtifactHash: Hash
    simulationStudyId: str
    simulationStudyVersion: int
    simulationStudyResourceVersion: Hash
    simulationStudyArtifactHash: Hash
    policyIntentDraftId: str
    policyIntentDraftVersion: int
    policyIntentDraftResourceVersion: Hash
    policyIntentDraftArtifactHash: Hash
    oracleProviderId: str
    oracleProviderResourceVersion: Hash
    oracleProviderAttestationHash: Hash
    oracleObservation: StrategyProposalAdmissionOracleObservation
    checks: StrategyProposalAdmissionChecks
    valid: bool
    validatedAt: str
    validUntil: str
    evidenceHashes: list[Hash]
    sourcePackage: NotRequired[StrategyPackageSourceLineage]

class ProposalWorkspaceExactTokenFlowsItem(TypedDict):
    token: Address
    amount: SignedAtomicAmount
    destination: Address

class ProposalWorkspaceAlternativesItem(TypedDict):
    label: str
    outcomeQuote: SignedAtomicAmount
    selected: bool

class ProposalWorkspaceInternalApprovalsItem(TypedDict):
    actorId: str
    approvedAt: str
    evidenceHash: Hash

class ProposalWorkspace(TypedDict):
    proposalId: str
    title: str
    rationale: str
    trigger: NotRequired[str]
    expectedImprovementQuote: SignedAtomicAmount
    maximumDownsideQuote: AtomicAmount
    costOfNoActionQuote: SignedAtomicAmount
    exactTokenFlows: list[ProposalWorkspaceExactTokenFlowsItem]
    beforeDepthQuote: AtomicAmount
    afterDepthQuote: AtomicAmount
    simulationStudyId: str
    strategyDefinitionId: str
    strategyValidationEventId: str
    strategyValidationArtifactHash: Hash
    alternatives: list[ProposalWorkspaceAlternativesItem]
    internalApprovalsRequired: int
    internalApprovals: list[ProposalWorkspaceInternalApprovalsItem]
    expiresAt: str
    safeTransactionIntent: NotRequired[ProposalSafeTransactionIntent]
    safeTransactionHash: NotRequired[Hash]

class ProposalWorkspaceInputExactTokenFlowsItem(TypedDict):
    token: Address
    amount: SignedAtomicAmount
    destination: Address

class ProposalWorkspaceInputAlternativesItem(TypedDict):
    label: str
    outcomeQuote: SignedAtomicAmount
    selected: bool

class ProposalWorkspaceInput(TypedDict):
    proposalId: str
    title: str
    rationale: str
    trigger: NotRequired[str]
    expectedImprovementQuote: SignedAtomicAmount
    maximumDownsideQuote: AtomicAmount
    costOfNoActionQuote: SignedAtomicAmount
    exactTokenFlows: list[ProposalWorkspaceInputExactTokenFlowsItem]
    beforeDepthQuote: AtomicAmount
    afterDepthQuote: AtomicAmount
    simulationStudyId: str
    strategyDefinitionId: str
    strategyValidationEventId: str
    strategyValidationArtifactHash: Hash
    alternatives: list[ProposalWorkspaceInputAlternativesItem]
    internalApprovalsRequired: int
    expiresAt: str
    safeTransactionIntent: NotRequired[ProposalSafeTransactionIntent]

class LaunchTimelineEvent(TypedDict):
    id: str
    kind: Literal["PRE_LAUNCH_SIMULATION", "INITIAL_FUNDING", "TGE", "FIRST_24_HOURS", "FIRST_7_DAYS", "MAINTENANCE_TRANSITION", "EXCHANGE_LISTING", "INCENTIVE_CHANGE", "TOKEN_UNLOCK", "TREASURY_DIVERSIFICATION"]
    scheduledAt: str
    reviewOwnerId: str
    dependsOn: list[str]
    requiresReview: bool
    status: Literal["PLANNED", "READY", "IN_REVIEW", "COMPLETED", "BLOCKED", "CANCELLED"]
    evidenceHashes: list[Hash]
    recommendationTrigger: NotRequired[str]
    reminderLeadSeconds: NotRequired[int]
    completedAt: NotRequired[str]
    completionReceiptHash: NotRequired[Hash]

class LaunchTimelineEventCreate(TypedDict):
    id: str
    kind: Literal["PRE_LAUNCH_SIMULATION", "INITIAL_FUNDING", "TGE", "FIRST_24_HOURS", "FIRST_7_DAYS", "MAINTENANCE_TRANSITION", "EXCHANGE_LISTING", "INCENTIVE_CHANGE", "TOKEN_UNLOCK", "TREASURY_DIVERSIFICATION"]
    scheduledAt: str
    reviewOwnerId: str
    dependsOn: list[str]
    requiresReview: bool
    status: Literal["PLANNED"]
    evidenceHashes: list[Hash]
    recommendationTrigger: NotRequired[str]
    reminderLeadSeconds: NotRequired[int]

class LaunchPlanInputSnapshot(TypedDict):
    schemaVersion: Literal["launch-plan-input-v1"]
    name: str
    tokenSupply: PositiveAtomicAmount
    treasuryAllocation: PositiveAtomicAmount
    launchValuationQuote: PositiveAtomicAmount
    liquidityBudgetQuote: PositiveAtomicAmount
    expectedInitialDemandQuote: PositiveAtomicAmount
    targetTradeSizeQuote: PositiveAtomicAmount
    maximumInitialSlippagePips: int
    acceptableInitialVolatilityPips: Pips
    initialPriceX18: PositiveAtomicAmount
    unlocks: list[UnlockTranche]
    reviewOwnerId: str
    launchAt: str

class LaunchPlan(TypedDict):
    calculationVersion: Literal["launch-plan-v2"]
    inputSnapshot: LaunchPlanInputSnapshot
    inputHash: Hash
    name: str
    tokenSupply: PositiveAtomicAmount
    treasuryAllocation: PositiveAtomicAmount
    launchValuationQuote: PositiveAtomicAmount
    liquidityBudgetQuote: PositiveAtomicAmount
    expectedInitialDemandQuote: PositiveAtomicAmount
    targetTradeSizeQuote: PositiveAtomicAmount
    maximumInitialSlippagePips: int
    acceptableInitialVolatilityPips: Pips
    initialPriceX18: PositiveAtomicAmount
    unlocks: list[UnlockTranche]
    recommendedInitialLiquidityQuote: PositiveAtomicAmount
    initialPriceLowerX18: AtomicAmount
    initialPriceUpperX18: AtomicAmount
    requiredReserveQuote: AtomicAmount
    bootstrapPhases: list[str]
    maintenanceTransition: list[str]
    emergencyPlaybook: list[str]
    timeline: list[LaunchTimelineEvent]

class UnlockImpactLaunchBinding(TypedDict):
    id: str
    version: int
    resourceVersion: Hash
    artifactHash: Hash

class UnlockImpactInputSnapshot(TypedDict):
    schemaVersion: Literal["unlock-impact-input-snapshot-v1"]
    unlocks: list[UnlockTranche]
    sourceLaunchPlan: Union[UnlockImpactLaunchBinding, None]
    sourceObservation: UnlockImpactSourceObservation

class MarketQualityObservationMetrics(TypedDict):
    targetTradeSizeQuote: PositiveAtomicAmount
    spreadPips: Pips
    concentrationPips: Pips
    volatilityImpactPips: Pips
    inventoryRiskPips: Pips
    imbalancePips: Pips
    recoverySeconds: int
    recoveryTargetSeconds: int

class MarketQualityRawMetrics(TypedDict):
    targetTradeSizeQuote: NotRequired[PositiveAtomicAmount]
    usableDepthQuote: NotRequired[AtomicAmount]
    deployedCapitalQuote: NotRequired[AtomicAmount]
    activeCapitalQuote: NotRequired[AtomicAmount]
    slippagePips: NotRequired[Pips]
    spreadPips: NotRequired[Pips]
    concentrationPips: NotRequired[Pips]
    volatilityImpactPips: NotRequired[Pips]
    inventoryRiskPips: NotRequired[Pips]
    imbalancePips: NotRequired[Pips]
    recoverySeconds: NotRequired[int]
    recoveryTargetSeconds: NotRequired[int]
    reliabilityPips: NotRequired[Pips]

class MarketQualityVenueSourceBinding(TypedDict):
    recordId: str
    observationId: str
    version: int
    resourceVersion: Hash
    artifactHash: Hash
    evidenceHash: Hash
    sourceProfileArtifactHash: Hash
    providerPayloadHash: Hash
    capturedAt: str

class MarketQualityExecutionSourceBinding(TypedDict):
    recordId: str
    proposalId: str
    version: int
    resourceVersion: Hash
    artifactHash: Hash
    finalizedAt: str

class MarketQualityCohortSourceBindingIssuersItem(TypedDict):
    issuerCommitmentHash: Hash
    score: int
    eligibilityEvidenceHash: Hash

class MarketQualityCohortSourceBinding(TypedDict):
    providerId: str
    providerResourceVersion: Hash
    providerAttestationHash: Hash
    cohortDefinitionId: str
    cohortDefinitionHash: Hash
    observedAt: str
    issuers: list[MarketQualityCohortSourceBindingIssuersItem]
    signature: str
    evidenceHash: Hash

class MarketQualityVaultSourceBinding(TypedDict):
    vaultId: str
    qualificationArtifactHash: Hash
    poolAddress: Address
    projectToken: Address
    quoteToken: Address
    venueId: str
    chainId: int

class MarketQualityPriorScoreSourceBinding(TypedDict):
    recordId: str
    version: int
    resourceVersion: Hash
    artifactHash: Hash
    capturedAt: str
    componentScoresHash: Hash

class MarketQualitySourceBindings(TypedDict):
    vault: MarketQualityVaultSourceBinding
    venueObservations: list[MarketQualityVenueSourceBinding]
    executionAttributions: list[MarketQualityExecutionSourceBinding]
    cohortEvidence: NotRequired[MarketQualityCohortSourceBinding]
    priorScore: NotRequired[MarketQualityPriorScoreSourceBinding]

class MarketQualityScoreComponentsItem(TypedDict):
    component: Literal["SLIPPAGE", "USABLE_DEPTH", "SPREAD", "CAPITAL_EFFICIENCY", "CONCENTRATION", "VOLATILITY_RESISTANCE", "INVENTORY_RISK", "IMBALANCE", "PRICE_RECOVERY", "RELIABILITY"]
    weightPips: Pips
    score: NotRequired[int]
    evidenceHashes: list[Hash]

class MarketQualityScoreChangeDriversItem(TypedDict):
    component: Literal["SLIPPAGE", "USABLE_DEPTH", "SPREAD", "CAPITAL_EFFICIENCY", "CONCENTRATION", "VOLATILITY_RESISTANCE", "INVENTORY_RISK", "IMBALANCE", "PRICE_RECOVERY", "RELIABILITY"]
    delta: int

class MarketQualityScorePeerBenchmark(TypedDict):
    cohortDefinition: str
    cohortSize: int
    percentile: int

class MarketQualityScore(TypedDict):
    scoreVersion: Literal["market-quality-score-v1", "market-quality-score-v2"]
    vaultId: str
    capturedAt: str
    rawMetrics: NotRequired[MarketQualityRawMetrics]
    sourceBindings: NotRequired[MarketQualitySourceBindings]
    inputHash: NotRequired[Hash]
    availability: Literal["AVAILABLE", "UNAVAILABLE"]
    score: NotRequired[int]
    coveragePips: Pips
    components: list[MarketQualityScoreComponentsItem]
    changeDrivers: list[MarketQualityScoreChangeDriversItem]
    improvements: list[str]
    peerBenchmark: NotRequired[MarketQualityScorePeerBenchmark]
    unavailableReason: NotRequired[str]

class ExecutionAttributionObservationHorizonsItem(TypedDict):
    kind: Literal["IMMEDIATE", "ADVERSE_SELECTION", "RECOVERY"]
    endedAt: str
    evidenceHash: Hash

class ExecutionAttributionMetricsItem(TypedDict):
    metric: Literal["SLIPPAGE", "FEES", "GAS", "INVENTORY", "CAPITAL_EFFICIENCY", "PRICE_MOVEMENT"]
    predicted: SignedAtomicAmount
    realized: SignedAtomicAmount
    residual: SignedAtomicAmount
    unit: Literal["QUOTE_ATOMIC", "TOKEN_ATOMIC", "PIPS"]

class ExecutionAttribution(TypedDict):
    attributionVersion: Literal["execution-attribution-v1"]
    proposalId: str
    transactionHash: Hash
    finalizedAt: str
    observationHorizonsComplete: bool
    sourceSimulationStudyId: str
    frozenForecastArtifactHash: Hash
    finalityEvidenceHash: Hash
    reconciliationEvidenceHash: Hash
    observationHorizons: list[ExecutionAttributionObservationHorizonsItem]
    metrics: list[ExecutionAttributionMetricsItem]
    adverseSelectionQuote: SignedAtomicAmount
    noActionCounterfactualQuote: SignedAtomicAmount
    realizedOutcomeQuote: SignedAtomicAmount
    calibrationResidualHash: Hash
    evidenceHashes: list[Hash]

class AnomalySubject(TypedDict):
    kind: Literal["VAULT"]
    vaultId: str

class AnomalyCurrentObservation(TypedDict):
    capturedAt: str
    value: SignedAtomicAmount
    evidenceHash: Hash

class AnomalySourceProvider(TypedDict):
    providerId: str
    providerResourceVersion: Hash
    providerAttestationHash: Hash
    observedAt: str
    payloadHash: Hash
    signature: str

class Anomaly(TypedDict):
    detectorVersion: Literal["robust-mad-v1"]
    subject: AnomalySubject
    evaluatedAt: str
    currentObservation: AnomalyCurrentObservation
    inputHash: NotRequired[Hash]
    derivationHash: NotRequired[Hash]
    sourceProvider: NotRequired[AnomalySourceProvider]
    kind: Literal["LIQUIDITY_DISAPPEARANCE", "ONE_SIDED_FLOW", "INACTIVE_RANGE", "STABLECOIN_DEPEG", "ORACLE_DISAGREEMENT", "INVENTORY_ACCUMULATION", "EXCESSIVE_TURNOVER", "MANIPULATION_INDICATOR", "SIMULATED_REALIZED_DIVERGENCE"]
    detected: bool
    severity: Literal["INFO", "WARNING", "CRITICAL"]
    median: SignedAtomicAmount
    medianAbsoluteDeviation: AtomicAmount
    deviationMultiplesPips: int
    coveragePips: Pips
    explanation: str
    responses: list[Literal["MONITOR", "TIGHTEN_POLICY", "PREPARE_REBALANCE", "PROTECT_RESERVE", "PAUSE"]]
    evidenceHashes: list[Hash]

class TreasuryBucket(TypedDict):
    entryId: str
    bucket: Literal["OPERATING_RESERVE", "EMERGENCY_RESERVE", "LIQUIDITY_CAPITAL", "DIVERSIFICATION_CAPITAL", "INCENTIVE_BUDGET", "STRATEGIC_RESERVE"]
    state: Literal["AVAILABLE", "DEPLOYED", "LOCKED", "AT_RISK", "FEE_GENERATING", "FUTURE_COMMITTED"]
    asset: Address
    amountAtomic: AtomicAmount
    valueQuote: AtomicAmount
    sourceKind: Literal["SAFE", "VAULT", "EXTERNAL_MANAGER", "SIGNED_OBLIGATION"]
    sourceId: str
    sourceObservationId: str
    capitalContainerId: str
    custodyLocationId: str
    obligationIds: list[str]
    futureCommittedValueQuote: AtomicAmount
    oracleSourceId: str
    oracleProviderResourceVersion: Hash
    oracleAttestationHash: Hash
    oracleEvidenceHash: Hash
    oracleSignature: str
    oracleObservedAt: str
    oracleMaximumAgeSeconds: int
    oracleConfidencePips: Pips
    bridgeHaircutPips: Pips
    counterpartyHaircutPips: Pips
    effectiveAt: str
    evidenceHash: Hash
    reconciliationEvidenceHash: Hash

class TreasurySummaryBucketsItem(TypedDict):
    bucket: Literal["OPERATING_RESERVE", "EMERGENCY_RESERVE", "LIQUIDITY_CAPITAL", "DIVERSIFICATION_CAPITAL", "INCENTIVE_BUDGET", "STRATEGIC_RESERVE"]
    grossValueQuote: AtomicAmount
    riskAdjustedValueQuote: AtomicAmount
    futureCommittedValueQuote: AtomicAmount
    uncommittedValueQuote: AtomicAmount
    byState: dict[str, AtomicAmount]

class TreasurySummaryAssetsItem(TypedDict):
    asset: Address
    grossValueQuote: AtomicAmount
    riskAdjustedValueQuote: AtomicAmount
    futureCommittedValueQuote: AtomicAmount
    uncommittedValueQuote: AtomicAmount

class TreasurySummaryContainersItem(TypedDict):
    capitalContainerId: str
    custodyLocationId: str
    asset: Address
    bucket: str
    state: str
    grossValueQuote: AtomicAmount
    futureCommittedValueQuote: AtomicAmount
    obligationIds: list[str]
    sourceObservationId: str

class TreasurySummaryConservation(TypedDict):
    bucketGrossValueQuote: AtomicAmount
    assetGrossValueQuote: AtomicAmount
    containerGrossValueQuote: AtomicAmount
    stateGrossValueQuote: AtomicAmount
    committedOverlayValueQuote: AtomicAmount
    conserved: bool
    evidenceHash: NotRequired[Hash]

class TreasurySummary(TypedDict):
    ledgerVersion: Literal["treasury-ledger-v1", "treasury-ledger-v2"]
    capturedAt: str
    grossValueQuote: AtomicAmount
    riskAdjustedValueQuote: AtomicAmount
    futureCommittedValueQuote: AtomicAmount
    uncommittedValueQuote: AtomicAmount
    buckets: list[TreasurySummaryBucketsItem]
    assets: list[TreasurySummaryAssetsItem]
    containers: list[TreasurySummaryContainersItem]
    duplicateSourceIds: list[str]
    duplicateEconomicKeys: list[str]
    staleEntryIds: list[str]
    invalidEntryIds: list[str]
    conservation: TreasurySummaryConservation
    complete: bool
    warnings: list[str]

class TreasuryStressStudyResultsItem(TypedDict):
    stressVersion: Literal["treasury-stress-v1", "treasury-stress-v2"]
    kind: Literal["TOKEN_PRICE_FALL_50", "STABLECOIN_DEPEG", "MAJOR_HOLDER_SELL", "LP_WITHDRAWAL", "EXCHANGE_DELISTING", "RUNWAY_DETERIORATION", "SIMULTANEOUS_UNLOCKS"]
    startingRiskAdjustedValueQuote: AtomicAmount
    stressedRiskAdjustedValueQuote: AtomicAmount
    lossQuote: AtomicAmount
    reserveSufficient: bool
    runwayDays: int
    bucketBreaches: list[str]
    liquidationCostQuote: AtomicAmount
    mitigations: list[str]
    policyLevel: NotRequired[Literal[0, 1, 2, 3, 4]]
    shockMagnitudePips: NotRequired[Pips]
    unlockSellPressureQuote: NotRequired[AtomicAmount]

class TreasuryStressStudy(TypedDict):
    stressSuiteVersion: Literal["treasury-stress-suite-v1"]
    evaluatedAt: str
    launchPlanId: str
    vaultId: str
    policyControlEpoch: AtomicAmount
    policyLevel: Literal[0, 1, 2, 3, 4]
    ledgerEvidenceHashes: list[Hash]
    unlockScheduleHash: Hash
    unlockImpactId: str
    unlockImpactResourceVersion: Hash
    unlockImpactArtifactHash: Hash
    policyArtifactHash: Hash
    results: list[TreasuryStressStudyResultsItem]
    allSevenShocksApplied: Literal[True]
    executionAuthorityGranted: Literal[False]

class VenueProfile(TypedDict):
    venueId: str
    chainId: int
    name: str
    kind: Literal["BDEX_V3", "EVM_V3", "EXTERNAL_MANAGER", "TREASURY_RESERVE"]
    writeAuthority: Literal["AUDITED_TYPED_ADAPTER", "READ_ONLY"]
    factoryAddress: NotRequired[Address]
    adapterRegistryAddress: NotRequired[Address]
    adapterAddress: NotRequired[Address]
    asset0: NotRequired[Address]
    asset1: NotRequired[Address]
    adapterRuntimeHash: NotRequired[Hash]
    controllerVenueId: NotRequired[Hash]
    poolHealthGuardAddress: NotRequired[Address]
    maximumTwapDeviationPips: NotRequired[Pips]
    maximumPositionWidthTicks: NotRequired[int]
    allowedActions: NotRequired[list[bool]]
    finalityBlocks: int
    reliabilityPips: Pips
    exitCostPips: Pips
    attestationHash: Hash

class VenueRpcQuorumAttestation(TypedDict):
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    memberId: str
    endpointId: str
    chainId: int
    chainGenesisHash: Hash
    finalizedBlockNumber: AtomicAmount
    finalizedBlockHash: Hash
    observationFactsHash: Hash
    observedAt: str
    signature: str

class VenueRpcQuorumVerification(TypedDict):
    verifierVersion: Literal["external-evm-rpc-quorum-v1", "onchain-market-maker-rpc-quorum-v1"]
    status: Literal["VERIFIED", "UNVERIFIED"]
    verifiedAt: str
    providerIds: list[str]
    memberIds: list[str]
    endpointIds: list[str]
    chainId: int
    chainGenesisHash: Hash
    finalizedBlockNumber: AtomicAmount
    finalizedBlockHash: Hash
    observationFactsHash: Hash
    agreementHash: Hash
    failureReasons: list[Literal["INSUFFICIENT_ATTESTATIONS", "DUPLICATE_PROVIDER", "DUPLICATE_MEMBER", "DUPLICATE_ENDPOINT", "UNKNOWN_PROVIDER", "PROVIDER_NOT_HEALTHY", "PROVIDER_GENERATION_MISMATCH", "PROVIDER_ATTESTATION_MISMATCH", "PROVIDER_SCOPE_MISMATCH", "STALE_ATTESTATION", "FUTURE_ATTESTATION", "CHAIN_MISMATCH", "GENESIS_MISMATCH", "FINALIZED_BLOCK_MISMATCH", "OBSERVATION_FACTS_MISMATCH", "INVALID_SIGNATURE"]]

class ProviderGatewayResponse(TypedDict):
    capability: str
    requestId: str
    attestationHash: Hash
    observedAt: str
    payloadHash: Hash
    payload: dict[str, object]
    signature: str

class PersistedProviderGatewayEvidence(TypedDict):
    providerId: str
    capability: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    providerPublicKeyFingerprint: Hash
    providerPublicKeySpkiBase64: str
    response: ProviderGatewayResponse

class ExternalVenueProviderEvidence(TypedDict):
    capability: Literal["EXTERNAL_VENUE_INDEXING"]
    providerId: str
    providerKeyResourceVersion: Hash
    providerPublicKeyFingerprint: Hash
    providerPublicKeySpkiBase64: str
    requestId: str
    observedAt: str
    attestationHash: Hash
    payloadHash: Hash
    signature: str

class VenueObservation(TypedDict):
    observationId: str
    vaultId: NotRequired[str]
    venueId: str
    poolAddress: NotRequired[Address]
    feeTierPips: NotRequired[Pips]
    assetMappingId: str
    deployedCapitalQuote: AtomicAmount
    activeCapitalQuote: AtomicAmount
    usableDepthQuote: AtomicAmount
    volumeQuote: AtomicAmount
    feesQuote: AtomicAmount
    slippagePips: Pips
    incentiveIncomeQuote: AtomicAmount
    fragmentationPips: Pips
    riskPips: Pips
    reliabilityPips: Pips
    bridgeHaircutPips: Pips
    marketQualityMetrics: NotRequired[MarketQualityObservationMetrics]
    capturedAt: str
    chainId: NotRequired[int]
    chainGenesisHash: NotRequired[Hash]
    finalizedBlockNumber: NotRequired[AtomicAmount]
    finalizedBlockHash: NotRequired[Hash]
    finalityEvidenceHash: NotRequired[Hash]
    rpcQuorumAttestations: NotRequired[list[VenueRpcQuorumAttestation]]
    rpcQuorumVerification: NotRequired[VenueRpcQuorumVerification]
    providerEvidence: NotRequired[ExternalVenueProviderEvidence]
    sourceVenueProfile: NotRequired[VenueProfileGenerationBinding]
    evidenceHash: Hash

class VenueAllocation(TypedDict):
    venueId: str
    allocationPips: Pips
    capitalQuote: AtomicAmount
    compositeScore: Pips
    writeAuthority: Literal["AUDITED_TYPED_ADAPTER", "READ_ONLY"]
    reasons: list[str]

class AllocationScoreVector(TypedDict):
    executionQualityPips: Pips
    feeYieldPips: Pips
    usableDepthPips: Pips
    capitalEfficiencyPips: Pips
    riskAdjustedSafetyPips: Pips
    fragmentationResistancePips: Pips
    exitFlexibilityPips: Pips

class AllocationPlanCandidate(TypedDict):
    candidateId: str
    objective: Literal["BALANCED", "EXECUTION_QUALITY", "CAPITAL_EFFICIENCY", "RISK_MINIMIZED", "EXIT_FLEXIBILITY"]
    allocations: list[VenueAllocation]
    scoreVector: AllocationScoreVector
    aggregateScorePips: Pips
    confidencePips: Pips
    executionClass: Literal["PREVIEW_ONLY", "BDEX_TYPED_EXECUTABLE"]

class AllocationPlanExcludedVenuesItem(TypedDict):
    venueId: str
    reasonCodes: list[Literal["UNKNOWN_VENUE", "PROFILE_STATUS_INELIGIBLE", "TREASURY_RESERVE_PROTECTED", "NO_MATCHING_OBSERVATION", "STALE_OBSERVATION", "FUTURE_OBSERVATION", "MISSING_PROVIDER_EVIDENCE", "ATTESTATION_MISMATCH", "MISSING_FINALITY_EVIDENCE", "MISSING_RPC_QUORUM"]]
    observedProfileStatus: NotRequired[OperatingSystemRecordStatus]
    profileResourceVersion: NotRequired[Hash]
    profileArtifactHash: NotRequired[Hash]

class AllocationPlan(TypedDict):
    allocatorVersion: Literal["multi-venue-pareto-v1"]
    intentName: str
    assetMappingId: str
    evaluatedAt: str
    totalCapitalQuote: AtomicAmount
    reservedCapitalQuote: AtomicAmount
    deployableCapitalQuote: AtomicAmount
    selectedCandidateId: str
    allocations: list[VenueAllocation]
    paretoFrontier: list[AllocationPlanCandidate]
    alternatives: list[AllocationPlanCandidate]
    currentPlanScorePips: Pips
    expectedPlanScorePips: Pips
    expectedScoreImprovementPips: int
    confidencePips: Pips
    excludedVenues: list[AllocationPlanExcludedVenuesItem]
    assumptions: list[str]
    executionClass: Literal["PREVIEW_ONLY", "BDEX_TYPED_EXECUTABLE"]

class ControllerVenueActionV2(TypedDict):
    kind: Literal[0, 1, 2, 3, 4, 5, 6]
    venueId: Hash
    asset0: Address
    asset1: Address
    assetIn: Address
    assetOut: Address
    amountIn: AtomicAmount
    minimumAmountOut: AtomicAmount
    amount0Max: AtomicAmount
    amount1Max: AtomicAmount
    amount0Min: AtomicAmount
    amount1Min: AtomicAmount
    positionId: AtomicAmount
    tickLower: int
    tickUpper: int
    liquidity: AtomicAmount
    sqrtPriceLimitX96: AtomicAmount
    deadline: AtomicAmount
    quoteHash: Hash

class ControllerExecutionBindingV2(TypedDict):
    schemaVersion: Literal["scheduled-liquidity-controller-action-v2"]
    functionName: Literal["executeSafeAction", "executeAutopilotAction", "executeScheduledLeg"]
    controllerAddress: Address
    adapterAddress: Address
    action: ControllerVenueActionV2
    actionId: NotRequired[Hash]
    planId: NotRequired[Hash]
    legIndex: NotRequired[int]
    proof: NotRequired[list[Hash]]
    calldata: str
    calldataHash: Hash

class ProposalSafeTransactionIntent(TypedDict):
    schemaVersion: Literal["proposal-controller-safe-intent-v1"]
    chainId: Literal[677, 968]
    vaultId: str
    vaultAddress: Address
    ownerSafe: Address
    venueId: str
    controllerExecution: ControllerExecutionBindingV2

class MigrationLegEconomicBindingV2(TypedDict):
    schemaVersion: Literal["migration-leg-economic-binding-v2"]
    legId: str
    capitalQuote: PositiveAtomicAmount
    asset0: Address
    asset1: Address
    quoteAsset: Address
    asset0Decimals: int
    asset1Decimals: int
    quoteDecimals: int
    asset0PriceQuoteX18: PositiveAtomicAmount
    asset1PriceQuoteX18: PositiveAtomicAmount
    expectedAmount0Atomic: AtomicAmount
    expectedAmount1Atomic: AtomicAmount
    valuationTolerancePips: int
    actionKind: Literal[1, 2, 3]
    actionPositionId: AtomicAmount
    actionLiquidity: AtomicAmount
    actionAmount0Max: AtomicAmount
    actionAmount1Max: AtomicAmount
    actionAmount0Min: AtomicAmount
    actionAmount1Min: AtomicAmount
    controllerActionHash: Hash
    oracleProviderId: str
    oracleProviderResourceVersion: Hash
    oracleProviderAttestationHash: Hash
    maximumAgeSeconds: int
    observedAt: str
    payloadHash: Hash
    signature: str

class MigrationPlanLeg(TypedDict):
    index: int
    legId: str
    route: Literal["FORWARD", "ROLLBACK"]
    kind: Literal["WITHDRAW", "HOLD_CHECKPOINT", "DEPLOY", "VERIFY", "ROLLBACK_CHECKPOINT", "ROLLBACK_WITHDRAW_TARGET", "ROLLBACK_REDEPLOY_SOURCE", "ROLLBACK_VERIFY_SOURCE"]
    venueId: str
    capitalQuote: AtomicAmount
    minimumDepthAfterQuote: AtomicAmount
    maximumSlippagePips: Pips
    dependsOnLegId: NotRequired[str]
    requiresPreviousLegFinalizedAndReconciled: bool
    conditional: bool
    controllerExecution: NotRequired[ControllerExecutionBindingV2]
    economicBinding: NotRequired[MigrationLegEconomicBindingV2]

class VenueProfileGenerationBinding(TypedDict):
    recordId: str
    recordVersion: int
    resourceVersion: Hash
    artifactHash: Hash
    status: Literal["VALIDATED", "ACTIVE"]
    venueId: str
    chainId: int
    kind: Literal["BDEX_V3", "EVM_V3", "EXTERNAL_MANAGER", "TREASURY_RESERVE"]
    writeAuthority: Literal["AUDITED_TYPED_ADAPTER", "READ_ONLY"]
    attestationHash: Hash
    adapterRegistryAddress: NotRequired[Address]
    adapterAddress: NotRequired[Address]
    adapterRuntimeHash: NotRequired[Hash]
    controllerVenueId: NotRequired[Hash]
    asset0: NotRequired[Address]
    asset1: NotRequired[Address]

MigrationVenueProfileBinding: TypeAlias = VenueProfileGenerationBinding

class MigrationPlan(TypedDict):
    plannerVersion: Literal["liquidity-migration-v1"]
    stateMachineVersion: Literal["liquidity-migration-state-v1"]
    executionVaultId: NotRequired[str]
    sourceVenueId: str
    targetVenueId: str
    sourceVenueBinding: MigrationVenueProfileBinding
    targetVenueBinding: MigrationVenueProfileBinding
    capitalQuote: AtomicAmount
    temporaryDepthReductionQuote: AtomicAmount
    expectedPriceImpactPips: Pips
    migrationCostQuote: AtomicAmount
    expectedMarketQualityImprovement: int
    executionClass: Literal["PREVIEW_ONLY", "AUDITED_TYPED_ADAPTER"]
    legs: list[MigrationPlanLeg]
    rollbackLegs: list[MigrationPlanLeg]
    rollbackReason: str
    assumptions: list[str]

class MigrationActionEnvelopeV2(TypedDict):
    schemaVersion: Literal["migration-action-envelope-v2"]
    actionIntentHash: Hash
    vaultId: str
    vaultAddress: Address
    controllerAddress: Address
    ownerSafe: Address
    controllerCalldata: str
    controllerCalldataHash: Hash

class MigrationVaultGenerationBindingV2DeploymentRuntimeHashes(TypedDict):
    module: Hash
    vault: Hash
    policyManager: Hash
    oracleGuard: Hash
    executionController: Hash
    executionRiskEngine: Hash

class MigrationVaultGenerationBindingV2(TypedDict):
    schemaVersion: Literal["migration-vault-generation-binding-v2"]
    vaultId: str
    updatedAt: str
    vaultAddress: Address
    controllerAddress: Address
    ownerSafe: Address
    deploymentProvenanceHash: Hash
    deploymentBlockHash: Hash
    deploymentRuntimeHashes: MigrationVaultGenerationBindingV2DeploymentRuntimeHashes
    policyStateGeneration: Union[str, None]
    controlStateGeneration: Union[str, None]

class OperatingSystemSubmissionReleaseRuntimeAuthorityV2NamedCappedVaultsItem(TypedDict):
    vaultId: str
    name: str
    vaultAddress: Address
    capitalCapAtomic: AtomicAmount
    evidenceHash: Hash

class OperatingSystemSubmissionReleaseRuntimeAuthorityV2ComponentsVenueAdapterRegistryV2(TypedDict):
    address: Address
    runtimeCodeHash: Hash

class OperatingSystemSubmissionReleaseRuntimeAuthorityV2ComponentsKlineOPrivateVaultV2(TypedDict):
    address: Address
    runtimeCodeHash: Hash

class OperatingSystemSubmissionReleaseRuntimeAuthorityV2ComponentsScheduledLiquidityControllerV2(TypedDict):
    address: Address
    runtimeCodeHash: Hash

class OperatingSystemSubmissionReleaseRuntimeAuthorityV2ComponentsBdexV3AdapterV2(TypedDict):
    address: Address
    runtimeCodeHash: Hash

class OperatingSystemSubmissionReleaseRuntimeAuthorityV2Components(TypedDict):
    venueAdapterRegistryV2: OperatingSystemSubmissionReleaseRuntimeAuthorityV2ComponentsVenueAdapterRegistryV2
    klineOPrivateVaultV2: OperatingSystemSubmissionReleaseRuntimeAuthorityV2ComponentsKlineOPrivateVaultV2
    scheduledLiquidityControllerV2: OperatingSystemSubmissionReleaseRuntimeAuthorityV2ComponentsScheduledLiquidityControllerV2
    bdexV3AdapterV2: OperatingSystemSubmissionReleaseRuntimeAuthorityV2ComponentsBdexV3AdapterV2

class OperatingSystemSubmissionReleaseRuntimeAuthorityV2EnabledAdapterCapsItemPerVenueCapsItem(TypedDict):
    maximumPerActionQuote: AtomicAmount
    maximumDailyTurnoverQuote: AtomicAmount

class OperatingSystemSubmissionReleaseRuntimeAuthorityV2EnabledAdapterCapsItemPerAssetCapsItem(TypedDict):
    asset: Address
    maximumPerAction: AtomicAmount
    maximumDailyTurnover: AtomicAmount

class OperatingSystemSubmissionReleaseRuntimeAuthorityV2EnabledAdapterCapsItem(TypedDict):
    venueId: str
    perVenueCaps: list[OperatingSystemSubmissionReleaseRuntimeAuthorityV2EnabledAdapterCapsItemPerVenueCapsItem]
    perAssetCaps: list[OperatingSystemSubmissionReleaseRuntimeAuthorityV2EnabledAdapterCapsItemPerAssetCapsItem]

class OperatingSystemSubmissionReleaseRuntimeAuthorityV2(TypedDict):
    releaseId: Hash
    chainId: Literal[677, 968]
    environment: Literal["testnet", "staging", "mainnet"]
    issuedAt: str
    expiresAt: str
    sourceCommit: Hash
    artifactDigest: Hash
    v1ReleaseDigest: Hash
    maximumAutonomyLevel: Literal[0, 1, 2, 3, 4]
    emergencyState: Literal["NORMAL", "PAUSED"]
    automatedExecution: bool
    publicMempoolFallback: bool
    bot968Live: bool
    bot677Live: bool
    namedCappedVaults: list[OperatingSystemSubmissionReleaseRuntimeAuthorityV2NamedCappedVaultsItem]
    externalEvmV3WriteAdaptersEnabled: Literal[False]
    components: OperatingSystemSubmissionReleaseRuntimeAuthorityV2Components
    enabledAdapterVenueIds: list[str]
    enabledAdapterCaps: list[OperatingSystemSubmissionReleaseRuntimeAuthorityV2EnabledAdapterCapsItem]

class OperatingSystemSubmissionReleaseAuthorityV2(TypedDict):
    schemaVersion: Literal["operating-system-submission-release-authority-v2"]
    releaseId: Hash
    releaseDigest: Hash
    feature: Literal["migrationPlanner", "protectedExecution"]
    featureState: Literal["LIVE"]
    cryptographicallyVerified: Literal[True]
    authorityEnabled: Literal[True]
    runtimeAuthority: OperatingSystemSubmissionReleaseRuntimeAuthorityV2
    runtimeAuthorityHash: Hash

class MigrationActionIntentV2(TypedDict):
    schemaVersion: Literal["migration-action-intent-v2"]
    releaseId: Hash
    chainId: Literal[677, 968]
    planId: str
    planRootHash: Hash
    route: Literal["FORWARD", "ROLLBACK"]
    leg: MigrationPlanLeg
    controllerExecution: ControllerExecutionBindingV2

class MigrationSubmissionAuthorityV2(TypedDict):
    schemaVersion: Literal["migration-submission-authority-v2"]
    releaseAuthority: OperatingSystemSubmissionReleaseAuthorityV2
    actionIntent: MigrationActionIntentV2
    actionIntentHash: Hash
    actionEnvelope: MigrationActionEnvelopeV2
    actionEnvelopeHash: Hash
    sourceVenueBinding: MigrationVenueProfileBinding
    targetVenueBinding: MigrationVenueProfileBinding
    vaultGeneration: MigrationVaultGenerationBindingV2
    safeVerificationEvidenceHash: Hash
    minimumFinalityDepth: int
    authorizationTransactionHash: Hash

class MigrationSkipTargetFactsV2(TypedDict):
    schemaVersion: Literal["migration-skip-target-facts-v2"]
    venueId: str
    controllerVenueId: Hash
    targetVenueProfileResourceVersion: Hash
    targetVenueProfileArtifactHash: Hash
    vaultId: str
    vaultUpdatedAt: str
    vaultGenerationHash: Hash
    factsBlockNumber: AtomicAmount
    factsBlockHash: Hash
    positionId: AtomicAmount
    positionExists: bool
    positionLiquidityAtomic: AtomicAmount
    positionAmount0Atomic: AtomicAmount
    positionAmount1Atomic: AtomicAmount
    issuerControlledPositionCount: int
    issuerControlledLiquidityAtomic: AtomicAmount
    issuerControlledAmount0Atomic: AtomicAmount
    issuerControlledAmount1Atomic: AtomicAmount
    targetVenueAsset0BalanceAtomic: AtomicAmount
    targetVenueAsset1BalanceAtomic: AtomicAmount
    vaultAsset0BalanceAtomic: AtomicAmount
    vaultAsset1BalanceAtomic: AtomicAmount
    usableDepthAfterQuote: AtomicAmount
    issuerControlledDepthQuote: AtomicAmount

class MigrationExecutionResultV2(TypedDict):
    schemaVersion: Literal["migration-execution-result-v2"]
    executionSucceeded: bool
    returnDataHash: Hash
    logsHash: Hash
    stateDeltaHash: Hash

class MigrationTransactionReceiptV2(TypedDict):
    schemaVersion: Literal["migration-transaction-receipt-v2"]
    actionEnvelopeHash: Hash
    submissionEvidenceHash: Hash
    transactionHash: Hash
    receiptStatus: Literal[0, 1]
    executionResult: MigrationExecutionResultV2
    executionResultHash: Hash
    finalizedBlockNumber: AtomicAmount
    finalizedBlockHash: Hash
    finalizedAt: str
    finalityDepth: int
    finalityEvidenceHash: Hash

class MigrationSkipSnapshotBindingV2(TypedDict):
    schemaVersion: Literal["migration-skip-snapshot-binding-v2"]
    actionIntentHash: Hash
    actionEnvelopeHash: Hash
    planId: str
    planRootHash: Hash
    previousStateHash: Hash
    priorLegStatus: Literal["READY"]
    route: Literal["ROLLBACK"]
    legId: str
    legKind: Literal["ROLLBACK_WITHDRAW_TARGET"]
    targetVenueBinding: MigrationVenueProfileBinding
    vaultGeneration: MigrationVaultGenerationBindingV2
    actionEnvelope: MigrationActionEnvelopeV2
    safeVerificationEvidenceHash: Hash
    minimumFinalityDepth: int

class MigrationSkipReconciliationSnapshotV2ActionUnnecessaryPredicate(TypedDict):
    predicateVersion: Literal["rollback-withdraw-target-unnecessary-v1"]
    result: Literal[True]
    predicateHash: Hash

class MigrationSkipReconciliationSnapshotV2(TypedDict):
    schemaVersion: Literal["migration-skip-reconciliation-snapshot-v2"]
    snapshotBinding: MigrationSkipSnapshotBindingV2
    snapshotBindingHash: Hash
    targetFacts: MigrationSkipTargetFactsV2
    targetFactsHash: Hash
    actionUnnecessaryPredicate: MigrationSkipReconciliationSnapshotV2ActionUnnecessaryPredicate
    finalizedBlockNumber: AtomicAmount
    finalizedBlockHash: Hash
    finalizedAt: str
    finalityDepth: int
    finalityEvidenceHash: Hash
    reconciliationBlockNumber: AtomicAmount
    reconciliationBlockHash: Hash
    reconciledAt: str
    reconciliationStatus: Literal["MATCHED"]
    reconciliationEvidenceHash: Hash
    observedAt: str

class MigrationPlanTransition(TypedDict):
    sequence: int
    legId: str
    route: Literal["FORWARD", "ROLLBACK"]
    fromStatus: Literal["BLOCKED", "READY", "SUBMITTED", "FINALIZED_RECONCILED", "FAILED_FINALIZED_RECONCILED", "SKIPPED_RECONCILED"]
    toStatus: Literal["SUBMITTED", "FINALIZED_RECONCILED", "FAILED_FINALIZED_RECONCILED", "SKIPPED_RECONCILED"]
    previousStateHash: Hash
    observedAt: str
    submissionEvidenceHash: NotRequired[Hash]
    transactionHash: NotRequired[Hash]
    submissionAuthority: NotRequired[MigrationSubmissionAuthorityV2]
    finalityEvidenceHash: NotRequired[Hash]
    reconciliationEvidenceHash: NotRequired[Hash]
    executionReceipt: NotRequired[MigrationTransactionReceiptV2]
    skipReconciliationSnapshot: NotRequired[MigrationSkipReconciliationSnapshotV2]

class MigrationPlanExecutionStateForwardLegsItem(TypedDict):
    legId: str
    route: Literal["FORWARD", "ROLLBACK"]
    status: Literal["BLOCKED", "READY", "SUBMITTED", "FINALIZED_RECONCILED", "FAILED_FINALIZED_RECONCILED", "SKIPPED_RECONCILED"]
    lastTransitionSequence: NotRequired[int]

class MigrationPlanExecutionStateRollbackLegsItem(TypedDict):
    legId: str
    route: Literal["FORWARD", "ROLLBACK"]
    status: Literal["BLOCKED", "READY", "SUBMITTED", "FINALIZED_RECONCILED", "FAILED_FINALIZED_RECONCILED", "SKIPPED_RECONCILED"]
    lastTransitionSequence: NotRequired[int]

class MigrationPlanExecutionState(TypedDict):
    stateMachineVersion: Literal["liquidity-migration-state-v1"]
    status: Literal["READY", "IN_PROGRESS", "COMPLETED", "ABORTED_RECONCILED", "ROLLBACK_READY", "ROLLING_BACK", "ROLLED_BACK", "FAILED_CLOSED"]
    forwardLegs: list[MigrationPlanExecutionStateForwardLegsItem]
    rollbackLegs: list[MigrationPlanExecutionStateRollbackLegsItem]
    transitionCount: int

class ControllerAssetLimitV2(TypedDict):
    asset: Address
    decimals: int
    maximumPerAction: AtomicAmount
    maximumDailyTurnover: AtomicAmount

class ControllerVenueAssetLimitV2(TypedDict):
    adapterId: str
    venueId: Hash
    asset: Address
    decimals: int
    maximumPerAction: AtomicAmount
    maximumDailyTurnover: AtomicAmount

class ControllerAdapterPermissionV2(TypedDict):
    adapterId: str
    adapter: Address
    poolHealthGuard: Address
    maximumTwapDeviationPips: int
    maximumPositionWidthTicks: int
    allowedActions: list[bool]

class ControllerCriticalDetectorPermissionV2(TypedDict):
    detectorId: Hash
    allowed: bool

class ControllerPolicyBindingV2(TypedDict):
    schemaVersion: Literal["scheduled-liquidity-controller-policy-v2"]
    executor: Address
    guardian: Address
    reconciler: Address
    priceGuard: Address
    floorBaseAsset: Address
    floorQuoteAsset: Address
    minimumReconciliationBlocks: int
    evidenceHash: Hash
    assetLimits: list[ControllerAssetLimitV2]
    venueLimits: list[ControllerVenueAssetLimitV2]
    adapterPermissions: list[ControllerAdapterPermissionV2]
    criticalDetectors: list[ControllerCriticalDetectorPermissionV2]

class ActivatedControllerPolicyV2Configuration(TypedDict):
    level: Literal[0, 1, 2, 3, 4]
    activationControlEpoch: AtomicAmount
    executor: Address
    guardian: Address
    reconciler: Address
    priceGuard: Address
    floorBaseAsset: Address
    floorQuoteAsset: Address
    cooldown: int
    maximumOracleAge: int
    expiresAtSeconds: AtomicAmount
    maximumSlippagePips: Pips
    minimumReconciliationBlocks: int
    priceFloorX18: AtomicAmount
    priceCeilingX18: AtomicAmount
    publicMempoolAllowed: bool
    evidenceHash: Hash

class ActivatedControllerPolicyV2AssetLimitsItem(TypedDict):
    asset: Address
    decimals: int
    maximumPerAction: AtomicAmount
    maximumDailyTurnover: AtomicAmount

class ActivatedControllerPolicyV2VenueLimitsItem(TypedDict):
    venueId: Hash
    asset: Address
    decimals: int
    maximumPerAction: AtomicAmount
    maximumDailyTurnover: AtomicAmount

class ActivatedControllerPolicyV2AdaptersItem(TypedDict):
    adapter: Address
    allowedActions: list[bool]

class ActivatedControllerPolicyV2DetectorsItem(TypedDict):
    detectorId: Hash
    allowed: bool

class ActivatedControllerPolicyV2(TypedDict):
    schemaVersion: Literal["activated-controller-policy-v2"]
    policyHash: Hash
    configuration: ActivatedControllerPolicyV2Configuration
    assetLimits: list[ActivatedControllerPolicyV2AssetLimitsItem]
    venueLimits: list[ActivatedControllerPolicyV2VenueLimitsItem]
    adapters: list[ActivatedControllerPolicyV2AdaptersItem]
    detectors: list[ActivatedControllerPolicyV2DetectorsItem]

class AutonomyPolicy(TypedDict):
    vaultId: str
    level: Literal[0, 1, 2, 3, 4]
    emergencyPaused: bool
    maximumAmountPerTransaction: AtomicAmount
    maximumDailyTurnover: AtomicAmount
    maximumSlippagePips: Pips
    approvedContracts: list[Address]
    approvedAssets: list[Address]
    approvedAdapterIds: list[str]
    minimumSecondsBetweenActions: int
    minimumPriceX18: NotRequired[AtomicAmount]
    maximumPriceX18: NotRequired[AtomicAmount]
    oracleMaximumAgeSeconds: int
    expiresAt: str
    controlEpoch: AtomicAmount
    publicMempoolFallbackAllowed: bool
    controllerBinding: NotRequired[ControllerPolicyBindingV2]
    activatedControllerPolicy: NotRequired[ActivatedControllerPolicyV2]
    approvedAt: NotRequired[str]
    safeTransactionHash: NotRequired[Hash]

class AutonomyPolicyInput(TypedDict):
    vaultId: str
    level: Literal[0, 1, 2, 3, 4]
    emergencyPaused: bool
    maximumAmountPerTransaction: AtomicAmount
    maximumDailyTurnover: AtomicAmount
    maximumSlippagePips: Pips
    approvedContracts: list[Address]
    approvedAssets: list[Address]
    approvedAdapterIds: list[str]
    minimumSecondsBetweenActions: int
    minimumPriceX18: NotRequired[AtomicAmount]
    maximumPriceX18: NotRequired[AtomicAmount]
    oracleMaximumAgeSeconds: int
    expiresAt: str
    controlEpoch: AtomicAmount
    publicMempoolFallbackAllowed: bool
    controllerBinding: NotRequired[ControllerPolicyBindingV2]

class PolicyIntentDraftClausesItem(TypedDict):
    field: Literal["EXECUTABLE_DEPTH_QUOTE", "PRICE_BAND_PIPS", "MAXIMUM_TREASURY_DEPLOYMENT_PIPS", "MAXIMUM_SLIPPAGE_PIPS", "MINIMUM_PRICE_X18", "MAXIMUM_DAILY_TURNOVER_PIPS", "COOLDOWN_SECONDS"]
    operator: Literal["EQ", "LTE", "GTE"]
    value: str
    unit: Literal["QUOTE_ATOMIC", "QUOTE_WHOLE_UNITS", "PIPS", "PRICE_X18", "SECONDS"]
    sourceStart: int
    sourceEnd: int
    confidencePips: Pips

class PolicyIntentDraft(TypedDict):
    sourceText: str
    extractionProvider: str
    extractionModel: str
    clauses: list[PolicyIntentDraftClausesItem]
    ambiguities: list[str]
    conflicts: list[str]
    normalizedAt: str

class ProtectedExecutionQuote(TypedDict):
    quoteId: str
    requestId: str
    typedActionIntentHash: Hash
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    routeKind: Literal["PRIVATE_AMM", "RFQ", "SOLVER", "PUBLIC_AMM"]
    amountIn: PositiveAtomicAmount
    amountOut: PositiveAtomicAmount
    gasCostQuote: AtomicAmount
    providerFeeQuote: AtomicAmount
    maximumSlippagePips: Pips
    expiresAt: str
    partialFillAllowed: bool
    minimumFillAmount: PositiveAtomicAmount
    settlementAdapterId: str
    signature: str
    evidenceHash: Hash

class ProtectedExecutionProviderBinding(TypedDict):
    providerId: str
    capability: Literal["PRIVATE_RELAY", "RFQ", "SOLVER", "RPC"]
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    providerVenueScope: list[str]

class ProtectedExecutionQuoteRequest(TypedDict):
    requestId: str
    vaultId: str
    chainId: int
    assetIn: Address
    assetOut: Address
    costQuoteAsset: Address
    settlementContract: Address
    settlementAdapterId: str
    amountIn: PositiveAtomicAmount
    maximumSlippagePips: Pips
    expiresAt: str
    createdAt: str
    autonomyPolicyId: str
    autonomyPolicyResourceVersion: Hash
    autonomyPolicyArtifactHash: Hash
    controlEpoch: AtomicAmount
    publicMempoolFallbackAllowed: bool
    typedActionIntentHash: Hash
    venueBinding: VenueProfileGenerationBinding
    providerBindings: list[ProtectedExecutionProviderBinding]

class ProtectedExecutionQuoteSet(TypedDict):
    requestId: str
    request: ProtectedExecutionQuoteRequest
    amountIn: PositiveAtomicAmount
    publicMempoolFallbackAllowed: bool
    quotes: list[ProtectedExecutionQuote]
    selectedQuoteId: NotRequired[str]
    unavailableReasons: list[str]

class ProtectedExecutionTypedAction(TypedDict):
    actionType: Literal["SWAP_EXACT_INPUT_V2"]
    chainId: int
    vaultId: str
    settlementAdapterId: str
    settlementContract: Address
    assetIn: Address
    assetOut: Address
    amountIn: PositiveAtomicAmount
    minimumAmountOut: PositiveAtomicAmount
    deadline: str
    quoteId: str
    childLegId: str
    policyControlEpoch: AtomicAmount
    controllerExecution: NotRequired[ControllerExecutionBindingV2]

class CanonicalEvmExecutionResultV1(TypedDict):
    schemaVersion: Literal["canonical-evm-execution-result-v1"]
    executionSucceeded: bool
    returnDataHash: Hash
    logsHash: Hash
    stateDeltaHash: Hash

class ProtectedExecutionActionEnvelopeV2(TypedDict):
    schemaVersion: Literal["protected-execution-action-envelope-v2"]
    releaseId: Hash
    chainId: Literal[677, 968]
    planId: str
    planRootHash: Hash
    quoteRequestId: str
    quoteSetArtifactHash: Hash
    autonomyPolicyId: str
    autonomyPolicyResourceVersion: Hash
    autonomyPolicyArtifactHash: Hash
    controlEpoch: AtomicAmount
    childLegId: str
    vaultId: str
    vaultAddress: Address
    controllerAddress: Address
    ownerSafe: Address
    typedAction: ProtectedExecutionTypedAction
    typedActionHash: Hash
    controllerExecution: ControllerExecutionBindingV2
    controllerCalldata: str
    controllerCalldataHash: Hash

class ProtectedExecutionSubmissionAuthorityV2(TypedDict):
    schemaVersion: Literal["protected-execution-submission-authority-v2"]
    releaseAuthority: OperatingSystemSubmissionReleaseAuthorityV2
    actionEnvelope: ProtectedExecutionActionEnvelopeV2
    actionEnvelopeHash: Hash
    policyArtifactHash: Hash
    activatedControllerPolicyHash: Hash
    venueBinding: VenueProfileGenerationBinding
    vaultGeneration: MigrationVaultGenerationBindingV2
    safeVerificationEvidenceHash: Hash
    minimumFinalityDepth: int
    authorizationTransactionHash: Hash

class ProtectedExecutionTransactionReceiptV2(TypedDict):
    schemaVersion: Literal["protected-execution-transaction-receipt-v2"]
    actionEnvelopeHash: Hash
    submissionEvidenceHash: Hash
    transactionHash: Hash
    receiptStatus: Literal[0, 1]
    executionResult: CanonicalEvmExecutionResultV1
    executionResultHash: Hash
    finalizedBlockNumber: AtomicAmount
    finalizedBlockHash: Hash
    finalizedAt: str
    finalityDepth: int
    finalityEvidenceHash: Hash

class ProtectedExecutionLegTransition(TypedDict):
    sequence: int
    childLegId: str
    fromStatus: Literal["PREPARED", "SUBMITTED", "FINALIZED_RECONCILED", "PAUSED", "FAILED"]
    toStatus: Literal["SUBMITTED", "FINALIZED_RECONCILED", "PAUSED", "FAILED"]
    previousStateHash: Hash
    observedAt: str
    decodedTypedActionHash: NotRequired[Hash]
    controllerControlEpoch: NotRequired[AtomicAmount]
    controllerActivePolicyHash: NotRequired[Hash]
    submissionEvidenceHash: NotRequired[Hash]
    submissionAuthority: NotRequired[ProtectedExecutionSubmissionAuthorityV2]
    transactionHash: NotRequired[Hash]
    finalityEvidenceHash: NotRequired[Hash]
    reconciliationEvidenceHash: NotRequired[Hash]
    failureEvidenceHash: NotRequired[Hash]
    executionReceipt: NotRequired[ProtectedExecutionTransactionReceiptV2]
    consumedAmountIn: NotRequired[AtomicAmount]
    residualAmountIn: NotRequired[AtomicAmount]
    amountOutReceived: NotRequired[AtomicAmount]

class ProtectedExecutionPlanChildLegsItem(TypedDict):
    childLegId: str
    index: int
    amountIn: PositiveAtomicAmount
    minimumAmountOut: PositiveAtomicAmount
    expiresAt: str
    state: Literal["PREPARED", "SUBMITTED", "FINALIZED_RECONCILED", "PAUSED", "FAILED"]
    typedAction: ProtectedExecutionTypedAction
    typedActionHash: NotRequired[Hash]
    submissionEvidenceHash: NotRequired[Hash]
    transactionHash: NotRequired[Hash]
    finalityEvidenceHash: NotRequired[Hash]
    reconciliationEvidenceHash: NotRequired[Hash]
    failureEvidenceHash: NotRequired[Hash]
    executionReceipt: NotRequired[ProtectedExecutionTransactionReceiptV2]
    consumedAmountIn: NotRequired[AtomicAmount]
    residualAmountIn: NotRequired[AtomicAmount]
    amountOutReceived: NotRequired[AtomicAmount]

class ProtectedExecutionPlan(TypedDict):
    planId: str
    quoteRequestId: str
    quoteSetResourceVersion: Hash
    quoteSetArtifactHash: Hash
    autonomyPolicyId: str
    autonomyPolicyResourceVersion: Hash
    autonomyPolicyArtifactHash: Hash
    controlEpoch: AtomicAmount
    publicMempoolFallbackAllowed: bool
    executionClass: Literal["PREVIEW_ONLY", "CONTROLLER_TYPED_EXECUTABLE"]
    executionUnavailableReasons: list[str]
    status: Literal["PREPARED", "IN_PROGRESS", "COMPLETED", "PAUSED", "FAILED_CLOSED"]
    selectedQuote: NotRequired[ProtectedExecutionQuote]
    netAmountOutQuote: AtomicAmount
    childLegs: list[ProtectedExecutionPlanChildLegsItem]
    transitions: list[ProtectedExecutionLegTransition]
    totalInputAmount: AtomicAmount
    totalConsumedAmount: AtomicAmount
    totalResidualAmount: AtomicAmount
    totalUnresolvedAmount: AtomicAmount
    totalAmountOutReceived: AtomicAmount
    fallbackQuoteId: NotRequired[str]
    requiresSafeApproval: bool
    pauseReason: NotRequired[Literal["PRIVATE_EXECUTION_UNAVAILABLE", "QUOTE_EXPIRED", "POLICY_CHANGED"]]

class StrategyPackageHistoricalTestsItem(TypedDict):
    studyId: str
    datasetHash: Hash
    reportHash: Hash
    compilerHash: Hash
    passedAt: str
    passed: Literal[True]

class StrategyPackageForkTestsItem(TypedDict):
    testRunId: str
    chainId: int
    forkBlockNumber: AtomicAmount
    forkBlockHash: Hash
    rpcQuorumEvidenceHashes: list[Hash]
    artifactHash: Hash
    compilerHash: Hash
    passedAt: str
    passed: Literal[True]

class StrategyPackageIndependentReviewsItem(TypedDict):
    reviewerIdentityId: str
    reviewerName: str
    reviewerOrganization: str
    reviewedPackageContentHash: Hash
    evidenceHash: Hash
    reviewedAt: str
    decision: Literal["APPROVE"]

class StrategyPackageApprovalRegistryEvidence(TypedDict):
    approvalId: str
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    packageId: str
    packageVersion: str
    packageContentHash: Hash
    compilerHash: Hash
    reviewSetHash: Hash
    issuedAt: str
    validUntil: str
    signature: str

class StrategyPackage(TypedDict):
    packageId: str
    publisherOrganizationId: str
    name: str
    version: str
    compilerVersion: Literal["strategy-dsl-v1"]
    packageContentHash: Hash
    compilerHash: Hash
    definition: StrategyDefinitionV2Input
    supportedAssetIds: list[str]
    supportedVenueIds: list[str]
    riskClass: Literal["LOW", "MODERATE", "HIGH", "EXPERIMENTAL"]
    performanceAssumptions: list[str]
    historicalTests: list[StrategyPackageHistoricalTestsItem]
    forkTests: list[StrategyPackageForkTestsItem]
    independentReviews: list[StrategyPackageIndependentReviewsItem]
    maximumCapitalQuote: AtomicAmount
    failureConditions: list[str]
    approvalRegistryEvidence: NotRequired[StrategyPackageApprovalRegistryEvidence]
    executionSurface: Literal["DECLARATIVE_NO_NETWORK_NO_SIGNING"]
    activationEligibility: Literal["DIGITAL_TWIN_ONLY", "ACTIVATION_WORKFLOW_ELIGIBLE", "REVOKED"]
    status: Literal["CANDIDATE", "APPROVED", "REVOKED"]

class PartnerLogoAsset(TypedDict):
    mediaType: Literal["image/png"]
    contentBase64: str
    contentHash: Hash

class PartnerTenantDomainVerificationsItem(TypedDict):
    domain: str
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    challengeHash: Hash
    observedAt: str
    validUntil: str
    signature: str

class PartnerTenant(TypedDict):
    partnerId: str
    name: str
    verifiedDomains: list[str]
    domainVerifications: list[PartnerTenantDomainVerificationsItem]
    domainVerificationHashes: dict[str, Hash]
    logoAsset: NotRequired[PartnerLogoAsset]
    accentColor: str
    terminology: dict[str, str]
    issuerOrganizationIds: list[str]
    portfolioReaderActorIds: list[str]
    proposalPreparerActorIds: list[str]
    reportBrandName: str
    supportEmail: NotRequired[str]
    contactName: NotRequired[str]
    description: NotRequired[str]

class PartnerIssuerConsent(TypedDict):
    consentId: str
    partnerId: str
    partnerOrganizationId: str
    issuerOrganizationId: str
    partnerConfigurationResourceVersion: Hash
    partnerConfigurationArtifactHash: Hash
    portfolioReaderActorIds: list[str]
    proposalPreparerActorIds: list[str]
    grantedAt: str
    expiresAt: NotRequired[str]
    state: Literal["ACTIVE", "REVOKED"]
    revokedAt: NotRequired[str]

class MarketMakerMandateObligationsItem(TypedDict):
    obligationId: str
    venueId: str
    minimumDepthQuote: AtomicAmount
    maximumSpreadPips: Pips
    minimumUptimePips: Pips

class MarketMakerMandateAmmBenchmark(TypedDict):
    capitalDeployedQuote: PositiveAtomicAmount
    usableDepthQuote: AtomicAmount
    observedSpreadPips: Pips
    costQuote: AtomicAmount
    reliabilityPips: Pips
    evidenceHashes: list[Hash]

class MarketMakerMandate(TypedDict):
    mandateId: str
    counterpartyName: str
    counterpartyIdentifier: str
    tokenLoanAtomic: AtomicAmount
    tokenLoanValueQuote: AtomicAmount
    stableAllocationQuote: AtomicAmount
    startsAt: str
    endsAt: str
    obligations: list[MarketMakerMandateObligationsItem]
    reportedInventoryToken: AtomicAmount
    reportedInventoryQuote: AtomicAmount
    returnedToken: AtomicAmount
    returnedTokenValueQuote: AtomicAmount
    repaidQuote: AtomicAmount
    managerCapitalDeployedQuote: PositiveAtomicAmount
    grossReturnsQuote: AtomicAmount
    usableDepthQuote: AtomicAmount
    costQuote: AtomicAmount
    counterpartyExposureQuote: AtomicAmount
    counterpartyExposureLimitQuote: PositiveAtomicAmount
    ammBenchmark: MarketMakerMandateAmmBenchmark
    evidenceHashes: list[Hash]

class MarketMakerEvidenceObservationChainEvidence(TypedDict):
    chainId: int
    chainGenesisHash: Hash
    blockNumber: AtomicAmount
    blockHash: Hash
    finality: Literal["FINALIZED"]
    rpcQuorumAttestations: list[VenueRpcQuorumAttestation]
    rpcQuorumVerification: NotRequired[VenueRpcQuorumVerification]

class MarketMakerEvidenceObservationBalancesItem(TypedDict):
    assetId: str
    amountAtomic: AtomicAmount
    valueQuote: AtomicAmount

class MarketMakerEvidenceObservation(TypedDict):
    observationId: str
    mandateId: str
    sourceKind: Literal["ONCHAIN_WALLET", "SIGNED_API", "SIGNED_FILE", "SIGNED_EXCHANGE"]
    observedAt: str
    sourceReferenceHash: Hash
    sourcePayloadHash: Hash
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    signature: str
    chainEvidence: NotRequired[MarketMakerEvidenceObservationChainEvidence]
    balances: list[MarketMakerEvidenceObservationBalancesItem]
    capitalDeployedQuote: AtomicAmount
    usableDepthQuote: AtomicAmount
    observedSpreadPips: Pips
    observedUptimePips: Pips
    grossReturnsQuote: AtomicAmount
    feesPaidQuote: AtomicAmount
    returnedToken: AtomicAmount
    returnedTokenValueQuote: AtomicAmount
    repaidQuote: AtomicAmount
    counterpartyExposureQuote: AtomicAmount
    reconciliationStatus: Literal["PENDING", "MATCHED", "DISPUTED", "FINALIZED"]
    reconciliationEvidenceHashes: list[Hash]
    evidenceHashes: list[Hash]

class MarketMakerEvidenceObservationInputVariant1BalancesItem(TypedDict):
    assetId: str
    amountAtomic: AtomicAmount
    valueQuote: AtomicAmount

class MarketMakerEvidenceObservationInputVariant1ChainEvidence(TypedDict):
    chainId: int
    chainGenesisHash: Hash
    blockNumber: AtomicAmount
    blockHash: Hash
    finality: Literal["FINALIZED"]
    rpcQuorumAttestations: list[VenueRpcQuorumAttestation]

class MarketMakerEvidenceObservationInputVariant1(TypedDict):
    observationId: str
    mandateId: str
    observedAt: str
    sourceReferenceHash: Hash
    sourcePayloadHash: Hash
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    signature: str
    balances: list[MarketMakerEvidenceObservationInputVariant1BalancesItem]
    capitalDeployedQuote: AtomicAmount
    usableDepthQuote: AtomicAmount
    observedSpreadPips: Pips
    observedUptimePips: Pips
    grossReturnsQuote: AtomicAmount
    feesPaidQuote: AtomicAmount
    returnedToken: AtomicAmount
    returnedTokenValueQuote: AtomicAmount
    repaidQuote: AtomicAmount
    counterpartyExposureQuote: AtomicAmount
    evidenceHashes: list[Hash]
    sourceKind: Literal["ONCHAIN_WALLET"]
    chainEvidence: MarketMakerEvidenceObservationInputVariant1ChainEvidence
    reconciliationStatus: Literal["PENDING", "DISPUTED"]
    reconciliationEvidenceHashes: list[Hash]

class MarketMakerEvidenceObservationInputVariant2BalancesItem(TypedDict):
    assetId: str
    amountAtomic: AtomicAmount
    valueQuote: AtomicAmount

class MarketMakerEvidenceObservationInputVariant2ChainEvidence(TypedDict):
    chainId: int
    chainGenesisHash: Hash
    blockNumber: AtomicAmount
    blockHash: Hash
    finality: Literal["FINALIZED"]
    rpcQuorumAttestations: list[VenueRpcQuorumAttestation]

class MarketMakerEvidenceObservationInputVariant2(TypedDict):
    observationId: str
    mandateId: str
    observedAt: str
    sourceReferenceHash: Hash
    sourcePayloadHash: Hash
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    signature: str
    balances: list[MarketMakerEvidenceObservationInputVariant2BalancesItem]
    capitalDeployedQuote: AtomicAmount
    usableDepthQuote: AtomicAmount
    observedSpreadPips: Pips
    observedUptimePips: Pips
    grossReturnsQuote: AtomicAmount
    feesPaidQuote: AtomicAmount
    returnedToken: AtomicAmount
    returnedTokenValueQuote: AtomicAmount
    repaidQuote: AtomicAmount
    counterpartyExposureQuote: AtomicAmount
    evidenceHashes: list[Hash]
    sourceKind: Literal["ONCHAIN_WALLET"]
    chainEvidence: MarketMakerEvidenceObservationInputVariant2ChainEvidence
    reconciliationStatus: Literal["MATCHED", "FINALIZED"]
    reconciliationEvidenceHashes: list[Hash]

class MarketMakerEvidenceObservationInputVariant3BalancesItem(TypedDict):
    assetId: str
    amountAtomic: AtomicAmount
    valueQuote: AtomicAmount

class MarketMakerEvidenceObservationInputVariant3(TypedDict):
    observationId: str
    mandateId: str
    observedAt: str
    sourceReferenceHash: Hash
    sourcePayloadHash: Hash
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    signature: str
    balances: list[MarketMakerEvidenceObservationInputVariant3BalancesItem]
    capitalDeployedQuote: AtomicAmount
    usableDepthQuote: AtomicAmount
    observedSpreadPips: Pips
    observedUptimePips: Pips
    grossReturnsQuote: AtomicAmount
    feesPaidQuote: AtomicAmount
    returnedToken: AtomicAmount
    returnedTokenValueQuote: AtomicAmount
    repaidQuote: AtomicAmount
    counterpartyExposureQuote: AtomicAmount
    evidenceHashes: list[Hash]
    sourceKind: Literal["SIGNED_API", "SIGNED_FILE", "SIGNED_EXCHANGE"]
    reconciliationStatus: Literal["PENDING", "DISPUTED"]
    reconciliationEvidenceHashes: list[Hash]

class MarketMakerEvidenceObservationInputVariant4BalancesItem(TypedDict):
    assetId: str
    amountAtomic: AtomicAmount
    valueQuote: AtomicAmount

class MarketMakerEvidenceObservationInputVariant4(TypedDict):
    observationId: str
    mandateId: str
    observedAt: str
    sourceReferenceHash: Hash
    sourcePayloadHash: Hash
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    signature: str
    balances: list[MarketMakerEvidenceObservationInputVariant4BalancesItem]
    capitalDeployedQuote: AtomicAmount
    usableDepthQuote: AtomicAmount
    observedSpreadPips: Pips
    observedUptimePips: Pips
    grossReturnsQuote: AtomicAmount
    feesPaidQuote: AtomicAmount
    returnedToken: AtomicAmount
    returnedTokenValueQuote: AtomicAmount
    repaidQuote: AtomicAmount
    counterpartyExposureQuote: AtomicAmount
    evidenceHashes: list[Hash]
    sourceKind: Literal["SIGNED_API", "SIGNED_FILE", "SIGNED_EXCHANGE"]
    reconciliationStatus: Literal["MATCHED", "FINALIZED"]
    reconciliationEvidenceHashes: list[Hash]

MarketMakerEvidenceObservationInput: TypeAlias = Union[MarketMakerEvidenceObservationInputVariant1, MarketMakerEvidenceObservationInputVariant2, MarketMakerEvidenceObservationInputVariant3, MarketMakerEvidenceObservationInputVariant4]

class MarketMakerOversightManager(TypedDict):
    capitalDeployedQuote: AtomicAmount
    usableDepthQuote: AtomicAmount
    spreadPips: Pips
    costQuote: AtomicAmount
    costPerDepthPips: Pips
    capitalEfficiencyPips: Pips
    reliabilityPips: Pips

class MarketMakerOversightAmmBenchmark(TypedDict):
    capitalDeployedQuote: AtomicAmount
    usableDepthQuote: AtomicAmount
    spreadPips: Pips
    costQuote: AtomicAmount
    costPerDepthPips: Pips
    capitalEfficiencyPips: Pips
    reliabilityPips: Pips

class MarketMakerOversightObligationAttainmentItem(TypedDict):
    obligationId: str
    venueId: str
    depthAttainmentPips: Pips
    spreadAttained: bool
    uptimeAttained: bool
    slaAttained: bool

class MarketMakerOversight(TypedDict):
    oversightVersion: Literal["market-maker-oversight-v1"]
    mandateId: str
    observationId: NotRequired[str]
    reconciliationStatus: Literal["PENDING", "MATCHED", "DISPUTED", "FINALIZED"]
    outstandingTokenLoanAtomic: AtomicAmount
    outstandingTokenLoanValueQuote: AtomicAmount
    outstandingStableAllocationQuote: AtomicAmount
    reportedAssetValueQuote: AtomicAmount
    grossReturnsQuote: AtomicAmount
    netReturnsQuote: SignedAtomicAmount
    counterpartyExposureQuote: AtomicAmount
    counterpartyRiskPips: Pips
    counterpartyExposureLimitBreached: bool
    manager: MarketMakerOversightManager
    ammBenchmark: MarketMakerOversightAmmBenchmark
    managerDepthAdvantageQuote: SignedAtomicAmount
    managerSpreadAdvantagePips: int
    managerCostPerDepthAdvantagePips: int
    managerCapitalEfficiencyAdvantagePips: int
    obligationAttainment: list[MarketMakerOversightObligationAttainmentItem]
    provenanceHashes: list[Hash]
    authorityBoundary: Literal["MONITORING_ONLY"]
    custodyAuthorityGranted: Literal[False]
    cexTradingAuthorityGranted: Literal[False]

IncentiveRecommendation: TypeAlias = Literal["INCREASE", "REDUCE", "RETARGET", "CHANGE_POOL", "CHANGE_RANGES", "REPLACE_WITH_TREASURY_LIQUIDITY", "MAINTAIN"]

class IncentiveProgramBaseline(TypedDict):
    baselineId: str
    method: Literal["PRE_PROGRAM_WINDOW", "MATCHED_CONTROL", "FROZEN_COUNTERFACTUAL"]
    windowStartsAt: str
    windowEndsAt: str
    frozenAt: str
    liquidityQuote: AtomicAmount
    volumeQuote: AtomicAmount
    slippagePips: Pips
    evidenceHashes: list[Hash]

class IncentiveProgramAdapterAuthorization(TypedDict):
    adapterId: str
    venueId: str
    adapterAddress: Address
    adapterRuntimeHash: Hash
    auditHash: Hash
    adapterManifestHash: Hash
    releasedManifestDigest: Hash
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    issuedAt: str
    validUntil: str
    allowedRecommendations: list[IncentiveRecommendation]
    signature: str

class IncentiveProgram(TypedDict):
    programId: str
    venueId: str
    startsAt: str
    endsAt: str
    incentivesPaidQuote: PositiveAtomicAmount
    claimedRewardsQuote: AtomicAmount
    baseline: IncentiveProgramBaseline
    observedLiquidityQuote: AtomicAmount
    observedVolumeQuote: AtomicAmount
    observedSlippagePips: Pips
    observedAt: str
    observationEvidenceHashes: list[Hash]
    retainedLiquidityQuote: AtomicAmount
    retentionObservedAt: str
    retentionEvidenceHashes: list[Hash]
    verifiedLiquidityDays: int
    confidencePips: Pips
    confidenceMethodology: str
    confidenceEvidenceHashes: list[Hash]
    requestedPoolId: NotRequired[str]
    requestedRangeId: NotRequired[str]
    adapterAuthorization: NotRequired[IncentiveProgramAdapterAuthorization]

class IncentiveOptimizationIncrementalLiquidityRangeQuote(TypedDict):
    low: SignedAtomicAmount
    high: SignedAtomicAmount

class IncentiveOptimizationIncrementalVolumeRangeQuote(TypedDict):
    low: SignedAtomicAmount
    high: SignedAtomicAmount

class IncentiveOptimization(TypedDict):
    optimizerVersion: Literal["incentive-optimizer-v1"]
    programId: str
    incrementalLiquidityQuote: SignedAtomicAmount
    incrementalVolumeQuote: SignedAtomicAmount
    incrementalLiquidityRangeQuote: IncentiveOptimizationIncrementalLiquidityRangeQuote
    incrementalVolumeRangeQuote: IncentiveOptimizationIncrementalVolumeRangeQuote
    slippageImprovementPips: int
    claimRatePips: Pips
    retentionPips: Pips
    costPerVerifiedLiquidityDayQuote: AtomicAmount
    mercenaryRiskPips: Pips
    recommendation: IncentiveRecommendation
    baselineEvidenceHashes: list[Hash]
    measurementEvidenceHashes: list[Hash]
    confidenceEvidenceHashes: list[Hash]
    reasons: list[str]

class LiquidityPassportRecordBinding(TypedDict):
    recordId: str
    recordVersion: int
    resourceVersion: Hash
    artifactHash: Hash

class LiquidityPassportSourceBindingsDepthRowsItem(TypedDict):
    rowIndex: int
    sourceKind: Literal["VENUE_OBSERVATION", "SIMULATION_STUDY"]
    source: LiquidityPassportRecordBinding
    venueProfile: NotRequired[LiquidityPassportRecordBinding]
    simulationVariant: NotRequired[Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]]
    sourceEvidenceHash: Hash

class LiquidityPassportSourceBindingsPositionReconciliation(TypedDict):
    vaultId: str
    vaultRecordHash: Hash
    vaultUpdatedAt: str
    snapshotId: str
    snapshotHash: Hash
    snapshotCapturedAt: str
    reconciliationRunId: str
    reconciliationEvidenceHash: Hash
    reconciliationBlockHash: Hash

class LiquidityPassportSourceBindingsIncidents(TypedDict):
    v1IncidentEvidenceHashes: list[Hash]
    anomalyEvidenceHashes: list[Hash]
    anomalyRecords: list[LiquidityPassportRecordBinding]

class LiquidityPassportSourceBindingsMarketMakerEvidenceItem(TypedDict):
    mandate: LiquidityPassportRecordBinding
    observationEventId: str
    observationArtifactHash: Hash
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    observedAt: str

class LiquidityPassportSourceBindingsReportArtifactsItem(TypedDict):
    reportId: str
    contentHash: Hash
    bundleHash: Hash
    publicationHash: NotRequired[Hash]

class LiquidityPassportSourceBindings(TypedDict):
    marketQualityScore: LiquidityPassportRecordBinding
    depthRows: list[LiquidityPassportSourceBindingsDepthRowsItem]
    autonomyPolicy: LiquidityPassportRecordBinding
    positionReconciliation: LiquidityPassportSourceBindingsPositionReconciliation
    incidents: LiquidityPassportSourceBindingsIncidents
    treasuryEntries: list[LiquidityPassportRecordBinding]
    marketMakerEvidence: list[LiquidityPassportSourceBindingsMarketMakerEvidenceItem]
    reportArtifacts: list[LiquidityPassportSourceBindingsReportArtifactsItem]

class LiquidityPassportReportBrandSourceBinding(TypedDict):
    partnerOrganizationId: str
    partnerConfigurationResourceVersion: Hash
    partnerConfigurationArtifactHash: Hash
    consentId: str
    consentResourceVersion: Hash
    consentArtifactHash: Hash

class LiquidityPassportReportBrand(TypedDict):
    partnerId: str
    name: str
    accentColor: str
    logoContentHash: NotRequired[Hash]
    sourceBinding: NotRequired[LiquidityPassportReportBrandSourceBinding]

class LiquidityPassportUsableDepthByTradeSizeItem(TypedDict):
    tradeSizeQuote: AtomicAmount
    buySlippagePips: Pips
    sellSlippagePips: Pips

class LiquidityPassportPolicyLimits(TypedDict):
    level: Literal[0, 1, 2, 3, 4]
    maximumAmountPerTransaction: AtomicAmount
    maximumDailyTurnover: AtomicAmount
    maximumSlippagePips: Pips
    approvedContracts: list[Address]
    approvedAssets: list[Address]
    approvedAdapterIds: list[str]
    minimumSecondsBetweenActions: int
    minimumPriceX18: NotRequired[AtomicAmount]
    maximumPriceX18: NotRequired[AtomicAmount]
    oracleMaximumAgeSeconds: int
    expiresAt: str
    controlEpoch: AtomicAmount
    publicMempoolFallbackAllowed: bool

class LiquidityPassportIncidentDetailsAnomaliesItem(TypedDict):
    detectorVersion: Literal["robust-mad-v1"]
    kind: Literal["LIQUIDITY_DISAPPEARANCE", "ONE_SIDED_FLOW", "INACTIVE_RANGE", "STABLECOIN_DEPEG", "ORACLE_DISAGREEMENT", "INVENTORY_ACCUMULATION", "EXCESSIVE_TURNOVER", "MANIPULATION_INDICATOR", "SIMULATED_REALIZED_DIVERGENCE"]
    severity: Literal["INFO", "WARNING", "CRITICAL"]
    artifactHash: Hash

class LiquidityPassportIncidentDetails(TypedDict):
    v1IncidentEvidenceHashes: list[Hash]
    anomalies: list[LiquidityPassportIncidentDetailsAnomaliesItem]

class LiquidityPassportDisclosure(TypedDict):
    showTreasuryOwnership: bool
    showExternalManagerNames: bool
    showIncidentDetails: bool
    showPolicyLimits: bool

class LiquidityPassportResultsRegistryReceipt(TypedDict):
    receiptVersion: Literal["liquidity-passport-results-registry-receipt-v1"]
    providerId: str
    providerResourceVersion: Hash
    providerAttestationHash: Hash
    passportSubjectHash: Hash
    commitmentHash: Hash
    issuedAt: str
    signature: str

class LiquidityPassport(TypedDict):
    passportVersion: Literal["liquidity-passport-v1"]
    artifactRendererVersion: Literal["liquidity-passport-artifacts-v1", "liquidity-passport-artifacts-v2"]
    signatureAlgorithm: Literal["Ed25519"]
    signerProviderId: str
    signerKeyResourceVersion: Hash
    slug: str
    vaultId: str
    issuerName: str
    reportBrand: NotRequired[LiquidityPassportReportBrand]
    generatedAt: str
    validUntil: str
    marketQualityScore: MarketQualityScore
    usableDepthByTradeSize: list[LiquidityPassportUsableDepthByTradeSizeItem]
    historicalReliabilityPips: Pips
    policyCompliancePips: Union[Pips, None]
    policyLimits: NotRequired[LiquidityPassportPolicyLimits]
    reconciledPositionCount: int
    majorIncidentCount: int
    treasuryOwnedLiquidityQuote: NotRequired[AtomicAmount]
    rentedLiquidityQuote: NotRequired[AtomicAmount]
    incidentDetails: NotRequired[LiquidityPassportIncidentDetails]
    externalManagerExposureQuote: NotRequired[AtomicAmount]
    externalManagerNames: NotRequired[list[str]]
    dataFreshnessSeconds: int
    disclosure: LiquidityPassportDisclosure
    reportHashes: list[Hash]
    sourceBindings: LiquidityPassportSourceBindings
    resultsRegistryProviderId: NotRequired[str]
    resultsRegistryProviderResourceVersion: NotRequired[Hash]
    resultsRegistryProviderAttestationHash: NotRequired[Hash]
    resultsRegistryCommitmentHash: NotRequired[Hash]
    resultsRegistryReceipt: NotRequired[LiquidityPassportResultsRegistryReceipt]
    supersedesPassportHash: NotRequired[Hash]
    contentHash: Hash
    signature: str

class OperatingSystemArtifact(TypedDict):
    organizationId: str
    contentHash: Hash
    recordType: str
    recordId: str
    recordVersion: int
    objectKey: str
    mediaType: str
    byteSize: AtomicAmount
    sourceHashes: list[Hash]
    retentionUntil: NotRequired[str]
    createdAt: str
    createdBy: str

class PublicPartnerBrandAccentTokens(TypedDict):
    darkPrimary: str
    darkPrimaryForeground: Literal["#000000", "#ffffff"]
    lightPrimary: str
    lightPrimaryForeground: Literal["#000000", "#ffffff"]

class PublicPartnerBrand(TypedDict):
    domain: str
    partnerId: str
    name: str
    reportBrandName: str
    supportEmail: NotRequired[str]
    logoPath: Union[str, None]
    terminology: dict[str, str]
    accentTokens: PublicPartnerBrandAccentTokens
    verificationHash: Hash
    configurationArtifactHash: Hash
    configurationVersion: int
    validUntil: str

class ApiError(TypedDict):
    code: str
    message: str
    remediation: NotRequired[str]
    correlationId: str
    retryable: bool
    fieldErrors: NotRequired[dict[str, list[str]]]

class PaginationMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class OperatingSystemEvent(TypedDict):
    organizationId: str
    eventId: str
    recordType: OperatingSystemRecordType
    recordId: str
    eventKind: str
    payload: dict[str, object]
    artifactHash: Hash
    createdBy: str
    actorRole: str
    reason: str
    requestId: str
    createdAt: str

class OperatingSystemJob(TypedDict):
    organizationId: str
    jobId: str
    lane: Literal["QUANTITATIVE_STUDIES", "EXTERNAL_VENUE_INDEXING", "ANOMALY_DETECTION", "PROPOSAL_SCHEDULING", "PROTECTED_EXECUTION_QUOTES", "WEBHOOK_DELIVERY", "REPORTING", "PARTNER_INTEGRATIONS", "AGENT_ORCHESTRATION"]
    aggregateType: str
    aggregateId: str
    requestPayload: dict[str, object]
    requestHash: Hash
    state: Literal["PENDING", "LEASED", "COMPLETED", "FAILED", "DEAD_LETTER"]
    attempts: int
    maximumAttempts: int
    availableAt: str
    leaseHolder: NotRequired[str]
    leaseExpiresAt: NotRequired[str]
    fencingToken: str
    result: NotRequired[dict[str, object]]
    lastErrorCode: NotRequired[str]
    createdAt: str
    updatedAt: str
    completedAt: NotRequired[str]

class OperatingSystemProvider(TypedDict):
    organizationId: str
    providerId: str
    capability: Literal["AI_EXTRACTION", "RPC", "ORACLE", "PRIVATE_RELAY", "RFQ", "SOLVER", "OBJECT_STORAGE", "WEBHOOK", "MARKET_MAKER", "INCENTIVE_ADAPTER", "PARTNER", "ISSUER_SIGNING", "RESULTS_REGISTRY", "STRATEGY_APPROVAL_REGISTRY", "DOMAIN_VERIFICATION", "EXECUTION_ATTRIBUTION"]
    chainScope: list[int]
    venueScope: list[str]
    attestationHash: Hash
    timeoutMilliseconds: int
    maximumAgeSeconds: int
    healthState: Literal["HEALTHY", "DEGRADED", "OPEN_CIRCUIT", "DISABLED"]
    consecutiveFailures: int
    circuitOpenUntil: NotRequired[str]
    responsePublicKey: str
    updatedAt: str
    resourceVersion: Hash

class StudyShareDisclosure(TypedDict):
    includeDrivers: bool
    includeTreasury: bool
    includePolicy: bool

class StudyShare(TypedDict):
    slug: str
    studyId: str
    visibility: Literal["PRIVATE", "PUBLIC"]
    expiresAt: str
    disclosure: StudyShareDisclosure
    approvedBy: str

class DeveloperCredential(TypedDict):
    credentialId: str
    label: str
    kind: Literal["API_KEY", "OAUTH_CLIENT"]
    scopes: list[Literal["scores:read", "studies:read", "studies:write", "strategies:validate", "policies:compile", "policies:check", "proposals:read", "proposals:prepare", "vaults:read", "receipts:read", "proof:read", "alerts:read", "webhooks:manage"]]
    keyPrefix: str
    secretHash: Hash
    createdAt: str
    expiresAt: NotRequired[str]
    rotatedAt: NotRequired[str]
    supersededSecretHash: NotRequired[Hash]

class WebhookSubscription(TypedDict):
    subscriptionId: str
    url: str
    eventTypes: list[str]
    secretHash: Hash
    active: bool
    maximumAttempts: Literal[8]
    createdAt: str
    secretReference: str

class QualifiedVaultV2(TypedDict):
    id: str
    organizationId: str
    name: str
    projectToken: Address
    quoteToken: Address
    ownerSafe: Address
    poolAddress: Union[Address, None]
    lifecycle: str
    mode: str
    runtimeVersion: str
    launchContext: Union[dict[str, object], None]
    capitalCapAtomic: Union[AtomicAmount, None]
    contracts: dict[str, object]
    deployment: dict[str, object]
    policy: Union[dict[str, object], None]
    control: dict[str, object]
    createdAt: str
    updatedAt: str
    artifactHash: Hash
    resourceVersion: Hash

class ExecutionReceiptV2(TypedDict):
    id: str
    organizationId: str
    vaultId: str
    proposalHash: Union[Hash, None]
    transactionHash: Union[Hash, None]
    status: Literal["FAILED_RECONCILED", "FINALIZED_RECONCILED_ATTRIBUTED", "FINALIZED_RECONCILED", "FINALIZED_PENDING_RECONCILIATION", "INCLUDED_PENDING_FINALITY"]
    inclusion: Union[dict[str, object], None]
    finality: Union[dict[str, object], None]
    reconciliation: Union[dict[str, object], None]
    attribution: Union[dict[str, object], None]
    failureAttribution: Union[dict[str, object], None]
    executionAttempts: list[dict[str, object]]
    sourceProposalState: str
    createdAt: str
    updatedAt: str
    artifactHash: Hash
    resourceVersion: Hash

class OAuthTokenResponse(TypedDict):
    access_token: str
    token_type: Literal["Bearer"]
    expires_in: int
    scope: str

class OperatingSystemStatus(TypedDict):
    status: Literal["AVAILABLE"]
    schemaVersion: Literal["klineo-token-liquidity-os-v2"]
    liveAuthority: Literal["SIGNED_V2_BOUNDARY", "FAIL_CLOSED"]
    executionAdapters: dict[str, object]
    release: dict[str, object]
    checkedAt: str

class StrategyCompilationIssuesItem(TypedDict):
    code: str
    severity: Literal["ERROR", "WARNING"]
    path: str
    message: str

class StrategyCompilationEnforceabilityItem(TypedDict):
    field: str
    class_: Literal["ONCHAIN", "DETERMINISTIC_OFFCHAIN", "MANUAL_APPROVAL"]
    reason: str

class StrategyCompilation(TypedDict):
    compilerVersion: Literal["strategy-dsl-v1"]
    valid: bool
    allocationPips: Pips
    issues: list[StrategyCompilationIssuesItem]
    enforceability: list[StrategyCompilationEnforceabilityItem]
    activationClass: Literal["BOUNDED_AUTOPILOT_ELIGIBLE", "SAFE_APPROVAL_ONLY", "INVALID"]

class CompiledPolicyIntentClausesItem(TypedDict):
    field: str
    operator: Literal["EQ", "LTE", "GTE"]
    value: str
    unit: Literal["QUOTE_ATOMIC", "QUOTE_WHOLE_UNITS", "PIPS", "PRICE_X18", "SECONDS"]
    sourceStart: int
    sourceEnd: int
    confidencePips: Pips
    enforceability: Literal["ONCHAIN", "DETERMINISTIC_OFFCHAIN", "MANUAL_APPROVAL"]

class CompiledPolicyIntent(TypedDict):
    compilerVersion: Literal["policy-intent-compiler-v1"]
    valid: bool
    clauses: list[CompiledPolicyIntentClausesItem]
    errors: list[str]
    warnings: list[str]
    confirmationSummary: list[str]

class OperatingSystemWorkspaceUnavailableItem(TypedDict):
    recordType: OperatingSystemRecordType
    recordId: str
    reason: str

class OperatingSystemWorkspaceWorkers(TypedDict):
    pending: int
    deadLetter: int

class OperatingSystemWorkspaceProvidersDegradedItem(TypedDict):
    providerId: str
    capability: Literal["AI_EXTRACTION", "RPC", "ORACLE", "PRIVATE_RELAY", "RFQ", "SOLVER", "OBJECT_STORAGE", "WEBHOOK", "MARKET_MAKER", "INCENTIVE_ADAPTER", "PARTNER", "ISSUER_SIGNING", "RESULTS_REGISTRY", "STRATEGY_APPROVAL_REGISTRY", "DOMAIN_VERIFICATION", "EXECUTION_ATTRIBUTION"]
    healthState: str

class OperatingSystemWorkspaceProviders(TypedDict):
    configured: int
    healthy: int
    degraded: list[OperatingSystemWorkspaceProvidersDegradedItem]

class OperatingSystemWorkspaceAuthority(TypedDict):
    aiExecutable: Literal[False]
    issuerSafeRequired: Literal[True]
    arbitraryCalldataAllowed: Literal[False]

class OperatingSystemWorkspace(TypedDict):
    schemaVersion: Literal["klineo-token-liquidity-os-v1"]
    role: str
    navigation: list[Literal["OPERATE", "PLAN", "SIMULATE", "STRATEGIES", "PROPOSALS", "INTELLIGENCE", "PROVE", "PLATFORM"]]
    releaseTrains: list[dict[str, object]]
    counts: dict[str, int]
    unavailable: list[OperatingSystemWorkspaceUnavailableItem]
    workers: OperatingSystemWorkspaceWorkers
    providers: OperatingSystemWorkspaceProviders
    authority: OperatingSystemWorkspaceAuthority

class UnifiedLiquidityMapVenuesItem(TypedDict):
    venueId: str
    assetMappingId: str
    deployedCapitalQuote: AtomicAmount
    activeCapitalQuote: AtomicAmount
    usableDepthQuote: AtomicAmount
    freshnessSeconds: int
    maximumAgeSeconds: int
    freshness: Literal["FRESH", "STALE", "FUTURE", "UNVERIFIED"]
    profileStatus: Literal["DRAFT", "VALIDATED", "ACTIVE", "PAUSED", "COMPLETED", "EXPIRED", "REVOKED", "SUPERSEDED", "UNAVAILABLE"]
    sourceProfileGenerationMatches: bool
    includedInTotals: bool

class UnifiedLiquidityMap(TypedDict):
    capturedAt: str
    availability: Literal["AVAILABLE", "DEGRADED", "UNAVAILABLE"]
    deployedCapitalQuote: AtomicAmount
    activeCapitalQuote: AtomicAmount
    usableDepthQuote: AtomicAmount
    venues: list[UnifiedLiquidityMapVenuesItem]
    warnings: list[str]

class ProposalDecisionResultProposal(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProposalWorkspace
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ProposalDecisionResultApprovalProgress(TypedDict):
    approved: int
    required: int

class ProposalDecisionResult(TypedDict):
    proposal: ProposalDecisionResultProposal
    decision: OperatingSystemEvent
    approvalProgress: NotRequired[ProposalDecisionResultApprovalProgress]
    rejectionReason: NotRequired[str]
    safeAuthorityGranted: Literal[False]

class ProposalSafeSubmissionResultProposal(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProposalWorkspace
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ProposalSafeSubmissionResult(TypedDict):
    proposal: ProposalSafeSubmissionResultProposal
    safeAuthorityEvidence: OperatingSystemEvent
    safeTransactionRegistered: Literal[True]
    executionPerformed: Literal[False]

class ProposalComparisonProposalsItem(TypedDict):
    id: str
    version: int
    title: str
    expectedImprovementQuote: SignedAtomicAmount
    maximumDownsideQuote: AtomicAmount
    costOfNoActionQuote: SignedAtomicAmount
    beforeDepthQuote: AtomicAmount
    afterDepthQuote: AtomicAmount
    approvalProgress: str
    expiresAt: str
    artifactHash: Hash

class ProposalComparison(TypedDict):
    comparedAt: str
    proposals: list[ProposalComparisonProposalsItem]
    immutableComparisonHash: Hash
    executionAuthorityGranted: Literal[False]

class LaunchTimelineTimelineItem(TypedDict):
    id: str
    kind: Literal["PRE_LAUNCH_SIMULATION", "INITIAL_FUNDING", "TGE", "FIRST_24_HOURS", "FIRST_7_DAYS", "MAINTENANCE_TRANSITION", "EXCHANGE_LISTING", "INCENTIVE_CHANGE", "TOKEN_UNLOCK", "TREASURY_DIVERSIFICATION"]
    scheduledAt: str
    reviewOwnerId: str
    dependsOn: list[str]
    requiresReview: bool
    status: Literal["PLANNED", "READY", "IN_REVIEW", "COMPLETED", "BLOCKED", "CANCELLED"]
    evidenceHashes: list[Hash]
    recommendationTrigger: NotRequired[str]
    reminderLeadSeconds: NotRequired[int]
    completedAt: NotRequired[str]
    completionReceiptHash: NotRequired[Hash]
    dependenciesComplete: bool

class LaunchTimeline(TypedDict):
    launchPlanId: str
    resourceVersion: Hash
    timeline: list[LaunchTimelineTimelineItem]
    evidenceHash: Hash

class LaunchWorkspaceSeedIssuerIntent(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: IssuerIntent
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class LaunchWorkspaceSeedCapitalRequirement(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: CapitalRequirementStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class LaunchWorkspaceSeedStrategy(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyDefinitionV2
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class LaunchWorkspaceSeedSimulationStudy(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: SimulationStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class LaunchWorkspaceSeedPolicyDraft(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PolicyIntentDraft
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class LaunchWorkspaceSeed(TypedDict):
    issuerIntent: LaunchWorkspaceSeedIssuerIntent
    capitalRequirement: LaunchWorkspaceSeedCapitalRequirement
    strategy: LaunchWorkspaceSeedStrategy
    strategyCompilation: StrategyCompilation
    simulationStudy: LaunchWorkspaceSeedSimulationStudy
    policyDraft: LaunchWorkspaceSeedPolicyDraft
    fundingProposal: None
    fundingProposalTemplate: dict[str, object]
    proposalPreparationBlockedBy: list[str]
    vaultQualification: dict[str, object]
    safeTransactionPrepared: Literal[False]
    executionPerformed: Literal[False]

class MigrationPlanStateResult(TypedDict):
    planId: str
    planResourceVersion: Hash
    state: MigrationPlanExecutionState
    stateHash: Hash
    executionClass: str
    executionAuthorized: Literal[False]
    readyLegIds: list[str]

class MigrationTransitionResult(TypedDict):
    event: OperatingSystemEvent
    state: MigrationPlanExecutionState
    stateHash: Hash
    executionClass: str
    executionAuthorized: Literal[True]
    evidenceAuthority: Literal["SERVER_VERIFIED_LEG_SPECIFIC"]
    evidenceHashes: list[Hash]

class PolicyCompilationResult(TypedDict):
    compilation: CompiledPolicyIntent
    executable: Literal[False]
    nextRequiredGates: list[Literal["USER_CONFIRMATION", "REVIEW", "SIMULATION", "TIMELOCK", "ISSUER_SAFE"]]

class PolicyDraftResultDraft(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PolicyIntentDraft
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class PolicyDraftResult(TypedDict):
    draft: PolicyDraftResultDraft
    compilationPreview: CompiledPolicyIntent
    executable: Literal[False]

class PolicyCheckResultCheck(TypedDict):
    compilerVersion: Literal["autonomy-policy-check-v1"]
    valid: bool
    errors: list[str]
    authorityExpansion: bool
    exactPolicyHash: Hash
    executable: Literal[False]
    activationGates: list[str]
    checkedAt: str

class PolicyCheckResultEvidence(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PolicyIntentDraft
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class PolicyCheckResult(TypedDict):
    check: PolicyCheckResultCheck
    evidence: PolicyCheckResultEvidence

class PartnerPortfolioBrand(TypedDict):
    name: str
    reportBrandName: str
    accentColor: str
    verifiedDomains: list[str]

class PartnerPortfolioIssuersItemVariant1MarketQualityVariant1(TypedDict):
    score: int
    capturedAt: str
    coveragePips: Pips
    artifactHash: Hash

class PartnerPortfolioIssuersItemVariant1MarketQualityVariant2(TypedDict):
    availability: Literal["UNAVAILABLE"]

class PartnerPortfolioIssuersItemVariant1ProposalsItem(TypedDict):
    proposalId: str
    title: str
    status: OperatingSystemRecordStatus
    expiresAt: str
    artifactHash: Hash

class PartnerPortfolioIssuersItemVariant1(TypedDict):
    issuerOrganizationId: str
    availability: Literal["AVAILABLE"]
    consentArtifactHash: Hash
    consentResourceVersion: Hash
    consentStatus: Literal["ACTIVE"]
    consentExpiresAt: Union[str, None]
    proposalPreparationScope: Literal["DECLARED", "NOT_DECLARED"]
    marketQuality: Union[PartnerPortfolioIssuersItemVariant1MarketQualityVariant1, PartnerPortfolioIssuersItemVariant1MarketQualityVariant2]
    venueCount: int
    proposals: list[PartnerPortfolioIssuersItemVariant1ProposalsItem]

class PartnerPortfolioIssuersItemVariant2(TypedDict):
    issuerOrganizationId: str
    availability: Literal["UNAVAILABLE_NO_BILATERAL_CONSENT"]

class PartnerPortfolio(TypedDict):
    schemaVersion: Literal["partner-portfolio-view-v2"]
    partnerId: str
    partnerConfigurationResourceVersion: Hash
    partnerConfigurationArtifactHash: Hash
    brand: PartnerPortfolioBrand
    issuers: list[Union[PartnerPortfolioIssuersItemVariant1, PartnerPortfolioIssuersItemVariant2]]
    generatedAt: str
    custodyAuthorityGranted: Literal[False]
    crossIssuerMutationAuthorityGranted: Literal[False]

class PartnerProposalPreparationResult(TypedDict):
    preparation: OperatingSystemEvent
    deliveryJobId: Union[str, None]
    issuerImportAndStandardApprovalRequired: Literal[True]
    safeAuthorityGranted: Literal[False]
    custodyAuthorityGranted: Literal[False]

class MarketMakerEvidenceResult(TypedDict):
    observation: OperatingSystemEvent
    oversight: MarketMakerOversight
    comparison: list[dict[str, object]]
    provenancePreserved: Literal[True]
    reconciliationStatus: Literal["PENDING", "MATCHED", "DISPUTED", "FINALIZED"]
    custodyAuthorityGranted: Literal[False]
    cexTradingAuthorityGranted: Literal[False]

class IncentiveOptimizationResultProgram(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: IncentiveProgram
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class IncentiveOptimizationResultWorkflow(TypedDict):
    mode: Literal["TYPED_ADAPTER_ACTIVATION_REVIEW", "OPERATIONAL_PROPOSAL_PREPARATION"]
    preparationHash: Hash
    evidenceEventId: str

class IncentiveOptimizationResult(TypedDict):
    program: IncentiveOptimizationResultProgram
    optimization: IncentiveOptimization
    workflow: IncentiveOptimizationResultWorkflow
    executionAuthority: Literal["STANDARD_TYPED_ADAPTER_ACTIVATION_WORKFLOW", "OPERATIONAL_PROPOSAL_ONLY"]
    executionPerformed: Literal[False]

class PublicPassportResultPublication(TypedDict):
    version: int
    artifactHash: Hash
    publishedAt: str
    supersedesVersion: Union[int, None]

class PublicPassportResultVerification(TypedDict):
    signatureValid: Literal[True]
    signatureAlgorithm: Literal["Ed25519"]
    signerProviderId: str
    signerKeyResourceVersion: Hash
    signerAttestationHash: Hash
    responsePublicKey: str
    publicKeyFingerprint: Hash
    trustAnchorState: Literal["CURRENT", "ROTATED"]
    verifiedAt: str

class PublicPassportResult(TypedDict):
    passport: LiquidityPassport
    publication: PublicPassportResultPublication
    verification: PublicPassportResultVerification

class LiquidityPassportVerificationBundlePublication(TypedDict):
    version: int
    artifactHash: Hash
    publishedAt: str
    supersedesVersion: Union[int, None]

class LiquidityPassportVerificationBundleVerification(TypedDict):
    signatureValid: Literal[True]
    signatureAlgorithm: Literal["Ed25519"]
    signerProviderId: str
    signerKeyResourceVersion: Hash
    signerAttestationHash: Hash
    responsePublicKey: str
    publicKeyFingerprint: Hash
    trustAnchorState: Literal["CURRENT", "ROTATED"]
    verifiedAt: str

class LiquidityPassportVerificationBundleArtifactsItem(TypedDict):
    format: Literal["JSON", "HTML", "PDF", "CSV"]
    mediaType: str
    fileName: str
    contentHash: Hash
    byteSize: AtomicAmount
    objectKey: str
    sourceHashes: list[Hash]
    providerEvidence: PersistedProviderGatewayEvidence
    downloadPath: str

class LiquidityPassportVerificationBundleResultsRegistryCommitmentVariant1(TypedDict):
    receiptVersion: Literal["liquidity-passport-results-registry-receipt-v1"]
    signatureAlgorithm: Literal["Ed25519"]
    providerId: str
    providerResourceVersion: Hash
    providerAttestationHash: Hash
    responsePublicKey: str
    publicKeyFingerprint: Hash
    trustAnchorState: Literal["CURRENT", "ROTATED"]
    passportSubjectHash: Hash
    commitmentHash: Hash
    issuedAt: str
    receiptSignature: str
    verificationState: Literal["PROVIDER_SIGNATURE_VERIFIED"]

class LiquidityPassportVerificationBundle(TypedDict):
    schemaVersion: Literal["klineo-liquidity-passport-verification-bundle-v1"]
    passport: LiquidityPassport
    publication: LiquidityPassportVerificationBundlePublication
    verification: LiquidityPassportVerificationBundleVerification
    artifacts: list[LiquidityPassportVerificationBundleArtifactsItem]
    sourceReportHashes: list[Hash]
    resultsRegistryCommitment: Union[LiquidityPassportVerificationBundleResultsRegistryCommitmentVariant1, None]

class SharedSimulationStudyShareDisclosure(TypedDict):
    includeDrivers: bool
    includeTreasury: bool
    includePolicy: bool

class SharedSimulationStudyShare(TypedDict):
    slug: str
    visibility: Literal["PRIVATE", "PUBLIC"]
    expiresAt: str
    disclosure: SharedSimulationStudyShareDisclosure

class SharedSimulationStudyStudy(TypedDict):
    id: str
    version: int
    status: OperatingSystemRecordStatus
    payload: DisclosedSimulationStudy
    artifactHash: Hash
    sourceArtifactHash: Hash
    updatedAt: str

class SharedSimulationStudyDisclosure(TypedDict):
    includeDrivers: bool
    includeTreasury: bool
    includePolicy: bool

class SharedSimulationStudy(TypedDict):
    share: SharedSimulationStudyShare
    study: SharedSimulationStudyStudy
    disclosure: SharedSimulationStudyDisclosure

class ProofResourceVariant1Record(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: LiquidityPassport
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ProofResourceVariant1(TypedDict):
    id: str
    kind: Literal["LIQUIDITY_PASSPORT"]
    status: OperatingSystemRecordStatus
    artifactHash: Hash
    resourceVersion: Hash
    createdAt: str
    updatedAt: str
    record: ProofResourceVariant1Record

class ProofResourceVariant2(TypedDict):
    id: str
    kind: Literal["CONTENT_ADDRESSED_ARTIFACT"]
    status: Literal["IMMUTABLE"]
    artifactHash: Hash
    resourceVersion: Hash
    createdAt: str
    updatedAt: str
    artifact: OperatingSystemArtifact

ProofResource: TypeAlias = Union[ProofResourceVariant1, ProofResourceVariant2]

class OpenApiDocument(TypedDict):
    openapi: str
    info: dict[str, object]
    servers: NotRequired[list[dict[str, object]]]
    paths: dict[str, dict[str, object]]
    components: dict[str, object]

class SimulationStudyRequest(TypedDict):
    issuerIntentId: str
    expectedIssuerIntentResourceVersion: Hash
    seed: str
    pathCount: Literal[2000, 10000]
    stepCount: int
    startingPortfolioQuote: PositiveAtomicAmount
    startingDepthQuote: PositiveAtomicAmount
    startingInventoryPips: Pips
    scenario: ScenarioDefinition
    reason: str

class SandboxSimulationStudyRequest(TypedDict):
    intent: IssuerIntent
    seed: str
    pathCount: Literal[2000]
    stepCount: int
    startingPortfolioQuote: PositiveAtomicAmount
    startingDepthQuote: PositiveAtomicAmount
    startingInventoryPips: Pips
    scenario: ScenarioDefinition
    reason: str

class StudyShareRequestVariant1Disclosure(TypedDict):
    includeDrivers: bool
    includeTreasury: bool
    includePolicy: bool

class StudyShareRequestVariant1(TypedDict):
    visibility: Literal["PRIVATE"]
    expiresAt: str
    disclosure: StudyShareRequestVariant1Disclosure
    reason: str

class StudyShareRequestVariant2Disclosure(TypedDict):
    includeDrivers: bool
    includeTreasury: bool
    includePolicy: bool

class StudyShareRequestVariant2(TypedDict):
    slug: NotRequired[str]
    visibility: Literal["PUBLIC"]
    expiresAt: str
    disclosure: StudyShareRequestVariant2Disclosure
    reason: str

StudyShareRequest: TypeAlias = Union[StudyShareRequestVariant1, StudyShareRequestVariant2]

class SignedStudyReportRequestDisclosure(TypedDict):
    includeDrivers: bool
    includeTreasury: bool
    includePolicy: bool

class SignedStudyReportRequest(TypedDict):
    formats: list[Literal["JSON", "PDF", "CSV"]]
    disclosure: SignedStudyReportRequestDisclosure
    reason: str

class StrategyProposalAdmissionRequestOracleEvidence(TypedDict):
    providerId: str
    providerResourceVersion: Hash
    observedAt: str
    payloadHash: Hash
    signature: str

class StrategyProposalAdmissionRequest(TypedDict):
    issuerIntentId: str
    simulationStudyId: str
    policyIntentDraftId: str
    oracleEvidence: StrategyProposalAdmissionRequestOracleEvidence
    reason: str

class ProposalCommentRequest(TypedDict):
    body: str
    mentions: list[str]
    supersedesCommentId: NotRequired[str]
    reason: str

class ProposalDecisionRequestVariant1(TypedDict):
    decision: Literal["APPROVE"]
    evidenceHash: Hash
    reason: str

class ProposalDecisionRequestVariant2(TypedDict):
    decision: Literal["REJECT"]
    rejectionReason: str
    evidenceHash: NotRequired[Hash]
    reason: str

ProposalDecisionRequest: TypeAlias = Union[ProposalDecisionRequestVariant1, ProposalDecisionRequestVariant2]

class ProposalSafeSubmissionRequest(TypedDict):
    reason: str

class ProposalComparisonRequest(TypedDict):
    proposalIds: list[str]
    reason: str

class LaunchPlanRequest(TypedDict):
    name: str
    tokenSupply: PositiveAtomicAmount
    treasuryAllocation: PositiveAtomicAmount
    launchValuationQuote: PositiveAtomicAmount
    liquidityBudgetQuote: PositiveAtomicAmount
    expectedInitialDemandQuote: PositiveAtomicAmount
    targetTradeSizeQuote: PositiveAtomicAmount
    maximumInitialSlippagePips: int
    acceptableInitialVolatilityPips: Pips
    initialPriceX18: PositiveAtomicAmount
    unlocks: list[UnlockTranche]
    reviewOwnerId: str
    launchAt: str
    reason: str

class TimelineEventRequest(TypedDict):
    payload: LaunchTimelineEventCreate
    reason: str

class TimelineCompletionRequest(TypedDict):
    completedAt: str
    completionReceiptHash: Hash
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class LaunchWorkspaceSeedRequest(TypedDict):
    vaultId: str
    projectTokenAddress: Address
    quoteTokenAddress: Address
    vaultAddress: Address
    quoteSymbol: str
    actionDeadline: NotRequired[str]
    reason: str

class UnlockImpactRequestVariant1(TypedDict):
    sourceLaunchPlanId: str
    unlockIds: NotRequired[list[str]]
    sourceObservation: UnlockImpactSourceObservation
    reason: str

class UnlockImpactRequestVariant2(TypedDict):
    unlocks: list[UnlockTranche]
    sourceObservation: UnlockImpactSourceObservation
    reason: str

UnlockImpactRequest: TypeAlias = Union[UnlockImpactRequestVariant1, UnlockImpactRequestVariant2]

class MarketQualityRequestSourceBindings(TypedDict):
    venueObservationIds: list[str]
    executionAttributionIds: list[str]

class MarketQualityRequestCohortEvidenceIssuersItem(TypedDict):
    issuerCommitmentHash: Hash
    score: int
    eligibilityEvidenceHash: Hash

class MarketQualityRequestCohortEvidence(TypedDict):
    providerId: str
    providerResourceVersion: Hash
    providerAttestationHash: Hash
    cohortDefinitionId: str
    cohortDefinitionHash: Hash
    observedAt: str
    issuers: list[MarketQualityRequestCohortEvidenceIssuersItem]
    signature: str

class MarketQualityRequest(TypedDict):
    vaultId: str
    capturedAt: str
    rawMetrics: MarketQualityRawMetrics
    sourceBindings: MarketQualityRequestSourceBindings
    cohortEvidence: NotRequired[MarketQualityRequestCohortEvidence]
    reason: str

class ExecutionAttributionRequestObservationEvidencePayloadObservationHorizonsItem(TypedDict):
    kind: Literal["IMMEDIATE", "ADVERSE_SELECTION", "RECOVERY"]
    endedAt: str
    evidenceHash: Hash

class ExecutionAttributionRequestObservationEvidencePayload(TypedDict):
    schemaVersion: Literal["execution-attribution-observation-v1"]
    proposalId: str
    transactionHash: Hash
    observationHorizons: list[ExecutionAttributionRequestObservationEvidencePayloadObservationHorizonsItem]
    adverseSelectionQuote: SignedAtomicAmount
    evidenceHashes: list[Hash]

class ExecutionAttributionRequestObservationEvidence(TypedDict):
    providerId: str
    providerResourceVersion: Hash
    providerAttestationHash: Hash
    observedAt: str
    payloadHash: Hash
    payload: ExecutionAttributionRequestObservationEvidencePayload
    signature: str

class ExecutionAttributionRequest(TypedDict):
    proposalId: str
    observationEvidence: ExecutionAttributionRequestObservationEvidence
    reason: str

class AnomalyDetectionRequestSubject(TypedDict):
    kind: Literal["VAULT"]
    vaultId: str

class AnomalyDetectionRequestObservationsItem(TypedDict):
    capturedAt: str
    value: SignedAtomicAmount
    evidenceHash: Hash

class AnomalyDetectionRequestCurrentObservation(TypedDict):
    capturedAt: str
    value: SignedAtomicAmount
    evidenceHash: Hash

class AnomalyDetectionRequestProviderEvidence(TypedDict):
    providerId: str
    providerResourceVersion: Hash
    providerAttestationHash: Hash
    observedAt: str
    payloadHash: Hash
    signature: str

class AnomalyDetectionRequest(TypedDict):
    subject: AnomalyDetectionRequestSubject
    kind: Literal["LIQUIDITY_DISAPPEARANCE", "ONE_SIDED_FLOW", "INACTIVE_RANGE", "STABLECOIN_DEPEG", "ORACLE_DISAGREEMENT", "INVENTORY_ACCUMULATION", "EXCESSIVE_TURNOVER", "MANIPULATION_INDICATOR", "SIMULATED_REALIZED_DIVERGENCE"]
    observations: list[AnomalyDetectionRequestObservationsItem]
    currentObservation: AnomalyDetectionRequestCurrentObservation
    minimumObservations: int
    thresholdMadMultiples: int
    providerEvidence: AnomalyDetectionRequestProviderEvidence
    reason: str

class CapitalRequirementRequest(TypedDict):
    issuerIntentId: str
    reason: str

class CapitalIntentSeedRequest(TypedDict):
    targetIssuerIntentId: NotRequired[str]
    reason: str

class CapitalLaunchSeedRequest(TypedDict):
    targetLaunchPlanId: NotRequired[str]
    name: str
    tokenSupply: PositiveAtomicAmount
    treasuryAllocation: PositiveAtomicAmount
    launchValuationQuote: PositiveAtomicAmount
    expectedInitialDemandQuote: PositiveAtomicAmount
    initialPriceX18: PositiveAtomicAmount
    unlocks: list[UnlockTranche]
    reviewOwnerId: str
    launchAt: str
    reason: str

class CapitalReservationRequest(TypedDict):
    reservationKind: Literal["MINIMUM_CAPITAL", "STABLE_RESERVE"]
    entryId: str
    bucket: Literal["OPERATING_RESERVE", "EMERGENCY_RESERVE", "LIQUIDITY_CAPITAL", "DIVERSIFICATION_CAPITAL", "INCENTIVE_BUDGET", "STRATEGIC_RESERVE"]
    asset: Address
    sourceId: str
    sourceObservationId: str
    capitalContainerId: str
    custodyLocationId: str
    obligationIds: list[str]
    oracleSourceId: str
    oracleProviderResourceVersion: Hash
    oracleAttestationHash: Hash
    oracleEvidenceHash: Hash
    oracleSignature: str
    oracleObservedAt: str
    oracleMaximumAgeSeconds: int
    oracleConfidencePips: Pips
    bridgeHaircutPips: Pips
    counterpartyHaircutPips: Pips
    effectiveAt: str
    evidenceHash: Hash
    reconciliationEvidenceHash: Hash
    reason: str

class TreasuryStressRequest(TypedDict):
    launchPlanId: str
    unlockImpactId: str
    unlockImpactResourceVersion: Hash
    unlockImpactArtifactHash: Hash
    vaultId: str
    monthlyOperatingCostQuote: PositiveAtomicAmount
    reason: str

class AllocationRequest(TypedDict):
    issuerIntentId: str
    totalCapitalQuote: PositiveAtomicAmount
    assetMappingId: str
    venueIds: list[str]
    reason: str

class MigrationRequestExecutionLegsItem(TypedDict):
    legId: Literal["forward-withdraw-source", "forward-deploy-target", "rollback-withdraw-target", "rollback-redeploy-source"]
    scheduledLegIndex: int
    proof: list[Hash]
    action: ControllerVenueActionV2
    economicBinding: MigrationLegEconomicBindingV2

class MigrationRequestExecution(TypedDict):
    vaultId: str
    scheduledPlanId: Hash
    legs: list[MigrationRequestExecutionLegsItem]

class MigrationRequest(TypedDict):
    sourceVenueId: str
    targetVenueId: str
    assetMappingId: str
    capitalQuote: PositiveAtomicAmount
    gasAndFeesQuote: AtomicAmount
    execution: NotRequired[MigrationRequestExecution]
    reason: str

class MigrationTransitionRequest(TypedDict):
    legId: str
    route: Literal["FORWARD", "ROLLBACK"]
    toStatus: Literal["SUBMITTED", "FINALIZED_RECONCILED", "FAILED_FINALIZED_RECONCILED", "SKIPPED_RECONCILED"]
    previousStateHash: Hash
    reason: str

class PolicyExtractRequest(TypedDict):
    sourceText: str
    reason: str

class StructuredPolicyRequestClausesItem(TypedDict):
    field: Literal["EXECUTABLE_DEPTH_QUOTE", "PRICE_BAND_PIPS", "MAXIMUM_TREASURY_DEPLOYMENT_PIPS", "MAXIMUM_SLIPPAGE_PIPS", "MINIMUM_PRICE_X18", "MAXIMUM_DAILY_TURNOVER_PIPS", "COOLDOWN_SECONDS"]
    operator: Literal["EQ", "LTE", "GTE"]
    value: AtomicAmount
    unit: Literal["QUOTE_ATOMIC", "PIPS", "PRICE_X18", "SECONDS"]

class StructuredPolicyRequest(TypedDict):
    clauses: list[StructuredPolicyRequestClausesItem]
    reason: str

class PolicyCheckRequest(TypedDict):
    policy: AutonomyPolicy
    previousPolicy: NotRequired[AutonomyPolicy]
    reason: str

class ProviderRegistrationRequest(TypedDict):
    providerId: str
    capability: Literal["AI_EXTRACTION", "RPC", "ORACLE", "PRIVATE_RELAY", "RFQ", "SOLVER", "OBJECT_STORAGE", "WEBHOOK", "MARKET_MAKER", "INCENTIVE_ADAPTER", "PARTNER", "ISSUER_SIGNING", "RESULTS_REGISTRY", "STRATEGY_APPROVAL_REGISTRY", "DOMAIN_VERIFICATION", "EXECUTION_ATTRIBUTION"]
    chainScope: list[int]
    venueScope: list[str]
    attestationHash: Hash
    timeoutMilliseconds: int
    maximumAgeSeconds: int
    healthState: Literal["HEALTHY", "DEGRADED", "OPEN_CIRCUIT", "DISABLED"]
    consecutiveFailures: int
    circuitOpenUntil: NotRequired[str]
    responsePublicKey: str
    reason: str

class DeveloperCredentialRequest(TypedDict):
    label: str
    kind: Literal["API_KEY", "OAUTH_CLIENT"]
    scopes: list[Literal["scores:read", "studies:read", "studies:write", "strategies:validate", "policies:compile", "policies:check", "proposals:read", "proposals:prepare", "vaults:read", "receipts:read", "proof:read", "alerts:read", "webhooks:manage"]]
    expiresAt: NotRequired[str]
    reason: str

class WebhookRequest(TypedDict):
    subscriptionId: NotRequired[str]
    url: str
    eventTypes: list[str]
    reason: str

class StrategyPackageCandidateHistoricalTestsItem(TypedDict):
    studyId: str
    datasetHash: Hash
    reportHash: Hash
    compilerHash: Hash
    passedAt: str
    passed: Literal[True]

class StrategyPackageCandidateForkTestsItem(TypedDict):
    testRunId: str
    chainId: int
    forkBlockNumber: AtomicAmount
    forkBlockHash: Hash
    rpcQuorumEvidenceHashes: list[Hash]
    artifactHash: Hash
    compilerHash: Hash
    passedAt: str
    passed: Literal[True]

class StrategyPackageCandidate(TypedDict):
    packageId: str
    publisherOrganizationId: str
    name: str
    version: str
    compilerVersion: Literal["strategy-dsl-v1"]
    compilerHash: Hash
    definition: StrategyDefinitionV2Input
    supportedAssetIds: list[str]
    supportedVenueIds: list[str]
    riskClass: Literal["LOW", "MODERATE", "HIGH", "EXPERIMENTAL"]
    performanceAssumptions: list[str]
    historicalTests: list[StrategyPackageCandidateHistoricalTestsItem]
    forkTests: list[StrategyPackageCandidateForkTestsItem]
    maximumCapitalQuote: AtomicAmount
    failureConditions: list[str]

class StrategyPackageApprovalRequestIndependentReviewsItem(TypedDict):
    reviewerIdentityId: str
    reviewerName: str
    reviewerOrganization: str
    reviewedPackageContentHash: Hash
    evidenceHash: Hash
    reviewedAt: str
    decision: Literal["APPROVE"]

class StrategyPackageApprovalRequestApprovalRegistryEvidence(TypedDict):
    approvalId: str
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    packageId: str
    packageVersion: str
    packageContentHash: Hash
    compilerHash: Hash
    reviewSetHash: Hash
    issuedAt: str
    validUntil: str
    signature: str

class StrategyPackageApprovalRequest(TypedDict):
    independentReviews: list[StrategyPackageApprovalRequestIndependentReviewsItem]
    approvalRegistryEvidence: StrategyPackageApprovalRequestApprovalRegistryEvidence
    reason: str

class StrategyPackageSeedRequest(TypedDict):
    targetStrategyId: str
    reason: str

class PartnerTenantCreateDomainVerificationsItem(TypedDict):
    domain: str
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    challengeHash: Hash
    observedAt: str
    validUntil: str
    signature: str

class PartnerTenantCreate(TypedDict):
    partnerId: str
    name: str
    domainVerifications: list[PartnerTenantCreateDomainVerificationsItem]
    logoAsset: NotRequired[PartnerLogoAsset]
    accentColor: str
    terminology: dict[str, str]
    issuerOrganizationIds: list[str]
    portfolioReaderActorIds: list[str]
    proposalPreparerActorIds: list[str]
    reportBrandName: str
    supportEmail: NotRequired[str]
    contactName: NotRequired[str]
    description: NotRequired[str]

class PartnerConsentOptions(TypedDict):
    partnerId: str
    partnerOrganizationId: str
    name: str
    partnerConfigurationResourceVersion: Hash
    partnerConfigurationArtifactHash: Hash
    portfolioReaderActorIds: list[str]
    proposalPreparerActorIds: list[str]
    status: Literal["ACTIVE"]
    currentConsentId: Union[str, None]

class PartnerPreparationContext(TypedDict):
    partnerId: str
    issuerOrganizationId: str
    partnerConfigurationResourceVersion: Hash
    partnerConfigurationArtifactHash: Hash
    consentId: str
    consentResourceVersion: Hash
    consentArtifactHash: Hash
    consentExpiresAt: Union[str, None]
    proposalPreparationAllowed: Literal[True]
    externalDeliveryAvailable: bool

class PartnerPreparationReceipt(TypedDict):
    preparationEventId: str
    preparationHash: Hash
    proposalId: str
    partnerId: str
    partnerOrganizationId: str
    partnerActorId: str
    issuerOrganizationId: str
    consentId: str
    consentResourceVersion: Hash
    consentArtifactHash: Hash
    partnerConfigurationResourceVersion: Hash
    partnerConfigurationArtifactHash: Hash
    deliveryJobId: Union[str, None]
    issuerImportAndStandardApprovalRequired: Literal[True]
    executionAuthorityGranted: Literal[False]
    safeAuthorityGranted: Literal[False]
    custodyAuthorityGranted: Literal[False]

class PartnerPreparationReceiptRecoveryVariant1(TypedDict):
    state: Literal["ACCEPTED"]
    receipt: PartnerPreparationReceipt

class PartnerPreparationReceiptRecoveryVariant2(TypedDict):
    state: Literal["UNRESOLVED"]

PartnerPreparationReceiptRecovery: TypeAlias = Union[PartnerPreparationReceiptRecoveryVariant1, PartnerPreparationReceiptRecoveryVariant2]

class PartnerPreparationInboxEntry(TypedDict):
    eventId: str
    consentId: str
    partnerId: str
    partnerOrganizationId: str
    partnerActorId: str
    createdAt: str
    preparationHash: Hash
    proposal: Union[ProposalWorkspace, None]
    consentResourceVersion: Hash
    consentArtifactHash: Hash
    status: Literal["PENDING", "IMPORTED", "DECLINED", "UNAVAILABLE"]
    unavailableReason: Union[str, None]
    importedProposalId: Union[str, None]
    executionAuthorityGranted: Literal[False]

class PartnerPreparationDecisionResultProposalVariant1(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProposalWorkspace
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class PartnerPreparationDecisionResult(TypedDict):
    decision: OperatingSystemEvent
    proposal: Union[PartnerPreparationDecisionResultProposalVariant1, None]
    issuerReviewRequired: bool
    executionAuthorityGranted: Literal[False]

class PartnerPreparationStatus(TypedDict):
    preparationEventId: str
    deliveryJobId: Union[str, None]
    deliveryState: Literal["NOT_REQUESTED", "PENDING", "LEASED", "COMPLETED", "FAILED", "DEAD_LETTER", "UNAVAILABLE"]
    lastErrorCode: Union[str, None]
    issuerDecision: Literal["PENDING", "IMPORTED", "DECLINED"]
    executionAuthorityGranted: Literal[False]

class PartnerDomainDnsRecord(TypedDict):
    type: Literal["TXT", "CNAME"]
    name: str
    value: str

class PartnerCustomHostname(TypedDict):
    id: str
    hostnameStatus: str
    sslStatus: str
    validationRecords: list[PartnerDomainDnsRecord]

class PartnerDomainChallengeVerificationVariant1(TypedDict):
    domain: str
    providerId: str
    providerKeyResourceVersion: Hash
    providerAttestationHash: Hash
    challengeHash: Hash
    observedAt: str
    validUntil: str
    signature: str

class PartnerDomainChallengeProvisioningOperationVariant1(TypedDict):
    id: str
    startedAt: str

class PartnerDomainChallenge(TypedDict):
    id: str
    organizationId: str
    partnerId: str
    domain: str
    createdBy: str
    createdAt: str
    expiresAt: str
    version: int
    challengeHash: Hash
    dns: PartnerDomainDnsRecord
    state: Literal["PENDING", "VERIFIED", "REVOKED"]
    verification: Union[PartnerDomainChallengeVerificationVariant1, None]
    customHostname: Union[PartnerCustomHostname, None]
    provisioningOperation: NotRequired[Union[PartnerDomainChallengeProvisioningOperationVariant1, None]]

class PartnerDomainStatus(TypedDict):
    challenge: PartnerDomainChallenge
    ownershipVerified: bool
    customHostname: Union[PartnerCustomHostname, None]
    cnameTarget: Union[str, None]
    dnsPointsToTarget: bool
    httpsReady: bool
    checkedAt: str
    provisioning: Literal["CLOUDFLARE_FOR_SAAS", "OPERATOR_MANAGED"]

class PartnerDomainChallengeCreateRequest(TypedDict):
    partnerId: str
    domain: str
    reason: str

class PartnerConsentGrantRequest(TypedDict):
    partnerId: str
    partnerOrganizationId: str
    partnerConfigurationResourceVersion: Hash
    partnerConfigurationArtifactHash: Hash
    portfolioReaderActorIds: list[str]
    proposalPreparerActorIds: list[str]
    expiresAt: NotRequired[str]
    reason: str

class MarketMakerEvidenceRequest(TypedDict):
    payload: MarketMakerEvidenceObservationInput
    reason: str

class MarketQualityScoreActivationRequest(TypedDict):
    reason: str

class TreasuryLedgerRefreshRequest(TypedDict):
    payload: TreasuryBucket
    reason: str

class TreasuryLedgerRetirementRequest(TypedDict):
    retirementEvidenceHash: Hash
    reason: str

class AgentControlCommandVariant1AssumptionsObjective(TypedDict):
    metric: Literal["ENDING_VALUE_P50", "MINIMUM_DEPTH_P5", "GAS_COST_P50", "DRAWDOWN_P95", "RESERVE_BREACH_PROBABILITY"]
    direction: Literal["MAXIMIZE", "MINIMIZE"]

class AgentControlCommandVariant1AssumptionsBaselineScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class AgentControlCommandVariant1AssumptionsBaselineScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[AgentControlCommandVariant1AssumptionsBaselineScenarioUnlocksItem]

class AgentControlCommandVariant1AssumptionsAlternativesItemScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class AgentControlCommandVariant1AssumptionsAlternativesItemScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[AgentControlCommandVariant1AssumptionsAlternativesItemScenarioUnlocksItem]

class AgentControlCommandVariant1AssumptionsAlternativesItem(TypedDict):
    label: str
    scenario: AgentControlCommandVariant1AssumptionsAlternativesItemScenario

class AgentControlCommandVariant1Assumptions(TypedDict):
    seed: NotRequired[str]
    stepCount: NotRequired[int]
    startingPortfolioQuote: NotRequired[str]
    startingDepthQuote: NotRequired[str]
    startingInventoryPips: NotRequired[int]
    objective: NotRequired[AgentControlCommandVariant1AssumptionsObjective]
    baselineScenario: NotRequired[AgentControlCommandVariant1AssumptionsBaselineScenario]
    alternatives: NotRequired[list[AgentControlCommandVariant1AssumptionsAlternativesItem]]

class AgentControlCommandVariant1(TypedDict):
    action: Literal["REVISE_ASSUMPTIONS"]
    questionId: str
    proposalHash: str
    assumptions: AgentControlCommandVariant1Assumptions

class AgentControlCommandVariant2Confirmation(TypedDict):
    proposalHash: str
    expectedSourceResourceVersion: str
    acceptedAcknowledgements: list[Literal["MODELED_STEPS_NOT_CALENDAR_DAYS", "CURRENT_DATA_NOT_HISTORICAL_REPLAY", "CURRENT_IS_PLANNER_GENERATED_NOT_ACTUAL_HOLDINGS", "UNLOCKS_AGGREGATED_AT_MIDPOINT", "NO_POSITIVE_BUYER_PRICE_IMPACT", "GAS_INCREASE_AT_MOST_TWO_TIMES", "QUOTE_IDENTITY_AND_DECIMALS_UNVERIFIED", "SCENARIOS_ARE_HYPOTHESES_NOT_FORECASTS", "UNLOCK_MAGNITUDE_IS_WEIGHTED_PARTICIPATION_PROXY", "HISTORICAL_RETURNS_ARE_FIXED_RETURN_MODEL_REPLAY", "DRIVER_ATTRIBUTION_IS_APPROXIMATE", "RESERVE_ORACLE_BREACH_IS_COMPOSITE_MODELED_EVENT"]]
    acceptProposedHypotheses: Literal[True]
    limitationsAccepted: Literal[True]

class AgentControlCommandVariant2(TypedDict):
    action: Literal["CONFIRM_RESEARCH"]
    questionId: str
    confirmation: AgentControlCommandVariant2Confirmation

class AgentControlCommandVariant3(TypedDict):
    action: Literal["CANCEL"]

class AgentControlCommandVariant4(TypedDict):
    action: Literal["RESPOND"]
    questionId: str
    optionId: str

AgentControlCommand: TypeAlias = Union[AgentControlCommandVariant1, AgentControlCommandVariant2, AgentControlCommandVariant3, AgentControlCommandVariant4]

class AgentControlReceipt(TypedDict):
    organizationId: str
    runId: str
    action: Literal["CANCEL", "RESPOND", "REVISE_ASSUMPTIONS", "CONFIRM_RESEARCH"]
    state: Literal["CANCELLED", "QUEUED", "COMPLETED"]
    successorRunId: NotRequired[Union[str, None]]
    resourceVersion: str
    acceptedAt: str
    replayed: bool

class ResearchPlanningStateSubject(TypedDict):
    issuerIntentId: str
    expectedResourceVersion: str

class ResearchPlanningStateProposalVariant1Subject(TypedDict):
    issuerIntentId: str
    expectedResourceVersion: str

class ResearchPlanningStateProposalVariant1CandidateObjective(TypedDict):
    metric: Literal["ENDING_VALUE_P50", "MINIMUM_DEPTH_P5", "GAS_COST_P50", "DRAWDOWN_P95", "RESERVE_BREACH_PROBABILITY"]
    direction: Literal["MAXIMIZE", "MINIMIZE"]

class ResearchPlanningStateProposalVariant1CandidateBaselineScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchPlanningStateProposalVariant1CandidateBaselineScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchPlanningStateProposalVariant1CandidateBaselineScenarioUnlocksItem]

class ResearchPlanningStateProposalVariant1CandidateAlternativesItemScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchPlanningStateProposalVariant1CandidateAlternativesItemScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchPlanningStateProposalVariant1CandidateAlternativesItemScenarioUnlocksItem]

class ResearchPlanningStateProposalVariant1CandidateAlternativesItem(TypedDict):
    label: str
    scenario: ResearchPlanningStateProposalVariant1CandidateAlternativesItemScenario

class ResearchPlanningStateProposalVariant1Candidate(TypedDict):
    seed: NotRequired[str]
    stepCount: NotRequired[int]
    startingPortfolioQuote: NotRequired[str]
    startingDepthQuote: NotRequired[str]
    startingInventoryPips: NotRequired[int]
    objective: NotRequired[ResearchPlanningStateProposalVariant1CandidateObjective]
    baselineScenario: NotRequired[ResearchPlanningStateProposalVariant1CandidateBaselineScenario]
    alternatives: list[ResearchPlanningStateProposalVariant1CandidateAlternativesItem]
    schemaVersion: Literal["research-experiment-v1"]
    pathCount: Literal[2000]
    interpretation: Literal["CURRENT_DATA_HYPOTHETICAL_MODELED_STEPS"]

class ResearchPlanningStateProposalVariant1ValidationIssuesItem(TypedDict):
    path: str
    message: str

class ResearchPlanningStateProposalVariant1ProvenanceItem(TypedDict):
    field: Literal["objective", "baselineScenario", "seed", "stepCount", "startingPortfolioQuote", "startingDepthQuote", "startingInventoryPips", "alternatives"]
    basis: Literal["USER_SUPPLIED_ASSUMPTION", "MODEL_PROPOSED_HYPOTHESIS", "MISSING"]

class ResearchPlanningStateProposalVariant1(TypedDict):
    schemaVersion: Literal["research-planning-proposal-v1"]
    organizationId: str
    runId: str
    contextHash: str
    sourceHash: str
    sourceCutoff: str
    subject: ResearchPlanningStateProposalVariant1Subject
    question: str
    status: Literal["NEEDS_INPUT", "NEEDS_REVIEW"]
    candidate: ResearchPlanningStateProposalVariant1Candidate
    missingInputs: list[Literal["objective", "baselineScenario", "seed", "stepCount", "startingPortfolioQuote", "startingDepthQuote", "startingInventoryPips"]]
    validationIssues: list[ResearchPlanningStateProposalVariant1ValidationIssuesItem]
    unsupportedRequests: list[Literal["CALENDAR_TIME", "HISTORICAL_AS_OF", "ACTUAL_HOLDINGS_BASELINE", "EXACT_UNLOCK_TIMING", "POSITIVE_BUYER_IMPACT", "GAS_ABOVE_TWO_TIMES", "UNLOCK_MARKET_DEPTH_IMPACT", "FILL_ACCURATE_BACKTEST", "OTHER_UNSUPPORTED"]]
    provenance: list[ResearchPlanningStateProposalVariant1ProvenanceItem]
    requiredAcknowledgements: list[Literal["MODELED_STEPS_NOT_CALENDAR_DAYS", "CURRENT_DATA_NOT_HISTORICAL_REPLAY", "CURRENT_IS_PLANNER_GENERATED_NOT_ACTUAL_HOLDINGS", "UNLOCKS_AGGREGATED_AT_MIDPOINT", "NO_POSITIVE_BUYER_PRICE_IMPACT", "GAS_INCREASE_AT_MOST_TWO_TIMES", "QUOTE_IDENTITY_AND_DECIMALS_UNVERIFIED", "SCENARIOS_ARE_HYPOTHESES_NOT_FORECASTS", "UNLOCK_MAGNITUDE_IS_WEIGHTED_PARTICIPATION_PROXY", "HISTORICAL_RETURNS_ARE_FIXED_RETURN_MODEL_REPLAY", "DRIVER_ATTRIBUTION_IS_APPROXIMATE", "RESERVE_ORACLE_BREACH_IS_COMPOSITE_MODELED_EVENT"]]
    financialAuthority: Literal[False]
    publicationAuthority: Literal[False]
    executionAuthorized: Literal[False]
    proposalHash: str

class ResearchPlanningState(TypedDict):
    schemaVersion: Literal["research-planning-state-v1"]
    organizationId: str
    runId: str
    runResourceVersion: str
    runState: Literal["QUEUED", "RUNNING", "WAITING_FOR_INPUT", "WAITING_FOR_CHILDREN", "COMPLETED", "PARTIAL", "ABSTAINED", "FAILED", "CANCELLED"]
    checkedAt: str
    subject: ResearchPlanningStateSubject
    currentSourceResourceVersion: Union[str, None]
    proposal: Union[ResearchPlanningStateProposalVariant1, None]
    questionId: Union[str, None]
    successorRunId: Union[str, None]

class ResearchPlanningAssumptionsObjective(TypedDict):
    metric: Literal["ENDING_VALUE_P50", "MINIMUM_DEPTH_P5", "GAS_COST_P50", "DRAWDOWN_P95", "RESERVE_BREACH_PROBABILITY"]
    direction: Literal["MAXIMIZE", "MINIMIZE"]

class ResearchPlanningAssumptionsBaselineScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchPlanningAssumptionsBaselineScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchPlanningAssumptionsBaselineScenarioUnlocksItem]

class ResearchPlanningAssumptionsAlternativesItemScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchPlanningAssumptionsAlternativesItemScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchPlanningAssumptionsAlternativesItemScenarioUnlocksItem]

class ResearchPlanningAssumptionsAlternativesItem(TypedDict):
    label: str
    scenario: ResearchPlanningAssumptionsAlternativesItemScenario

class ResearchPlanningAssumptions(TypedDict):
    seed: NotRequired[str]
    stepCount: NotRequired[int]
    startingPortfolioQuote: NotRequired[str]
    startingDepthQuote: NotRequired[str]
    startingInventoryPips: NotRequired[int]
    objective: NotRequired[ResearchPlanningAssumptionsObjective]
    baselineScenario: NotRequired[ResearchPlanningAssumptionsBaselineScenario]
    alternatives: NotRequired[list[ResearchPlanningAssumptionsAlternativesItem]]

class ResearchPlanningAdmissionRequestSubject(TypedDict):
    issuerIntentId: str
    expectedResourceVersion: str

class ResearchPlanningAdmissionRequestAssumptionsObjective(TypedDict):
    metric: Literal["ENDING_VALUE_P50", "MINIMUM_DEPTH_P5", "GAS_COST_P50", "DRAWDOWN_P95", "RESERVE_BREACH_PROBABILITY"]
    direction: Literal["MAXIMIZE", "MINIMIZE"]

class ResearchPlanningAdmissionRequestAssumptionsBaselineScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchPlanningAdmissionRequestAssumptionsBaselineScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchPlanningAdmissionRequestAssumptionsBaselineScenarioUnlocksItem]

class ResearchPlanningAdmissionRequestAssumptionsAlternativesItemScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchPlanningAdmissionRequestAssumptionsAlternativesItemScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchPlanningAdmissionRequestAssumptionsAlternativesItemScenarioUnlocksItem]

class ResearchPlanningAdmissionRequestAssumptionsAlternativesItem(TypedDict):
    label: str
    scenario: ResearchPlanningAdmissionRequestAssumptionsAlternativesItemScenario

class ResearchPlanningAdmissionRequestAssumptions(TypedDict):
    seed: NotRequired[str]
    stepCount: NotRequired[int]
    startingPortfolioQuote: NotRequired[str]
    startingDepthQuote: NotRequired[str]
    startingInventoryPips: NotRequired[int]
    objective: NotRequired[ResearchPlanningAdmissionRequestAssumptionsObjective]
    baselineScenario: NotRequired[ResearchPlanningAdmissionRequestAssumptionsBaselineScenario]
    alternatives: NotRequired[list[ResearchPlanningAdmissionRequestAssumptionsAlternativesItem]]

class ResearchPlanningAdmissionRequest(TypedDict):
    kind: Literal["WHAT_IF_RESEARCH"]
    mode: Literal["PLAN"]
    question: str
    subject: ResearchPlanningAdmissionRequestSubject
    assumptions: ResearchPlanningAdmissionRequestAssumptions

class ResearchPlanningProposalSubject(TypedDict):
    issuerIntentId: str
    expectedResourceVersion: str

class ResearchPlanningProposalCandidateObjective(TypedDict):
    metric: Literal["ENDING_VALUE_P50", "MINIMUM_DEPTH_P5", "GAS_COST_P50", "DRAWDOWN_P95", "RESERVE_BREACH_PROBABILITY"]
    direction: Literal["MAXIMIZE", "MINIMIZE"]

class ResearchPlanningProposalCandidateBaselineScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchPlanningProposalCandidateBaselineScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchPlanningProposalCandidateBaselineScenarioUnlocksItem]

class ResearchPlanningProposalCandidateAlternativesItemScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchPlanningProposalCandidateAlternativesItemScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchPlanningProposalCandidateAlternativesItemScenarioUnlocksItem]

class ResearchPlanningProposalCandidateAlternativesItem(TypedDict):
    label: str
    scenario: ResearchPlanningProposalCandidateAlternativesItemScenario

class ResearchPlanningProposalCandidate(TypedDict):
    seed: NotRequired[str]
    stepCount: NotRequired[int]
    startingPortfolioQuote: NotRequired[str]
    startingDepthQuote: NotRequired[str]
    startingInventoryPips: NotRequired[int]
    objective: NotRequired[ResearchPlanningProposalCandidateObjective]
    baselineScenario: NotRequired[ResearchPlanningProposalCandidateBaselineScenario]
    alternatives: list[ResearchPlanningProposalCandidateAlternativesItem]
    schemaVersion: Literal["research-experiment-v1"]
    pathCount: Literal[2000]
    interpretation: Literal["CURRENT_DATA_HYPOTHETICAL_MODELED_STEPS"]

class ResearchPlanningProposalValidationIssuesItem(TypedDict):
    path: str
    message: str

class ResearchPlanningProposalProvenanceItem(TypedDict):
    field: Literal["objective", "baselineScenario", "seed", "stepCount", "startingPortfolioQuote", "startingDepthQuote", "startingInventoryPips", "alternatives"]
    basis: Literal["USER_SUPPLIED_ASSUMPTION", "MODEL_PROPOSED_HYPOTHESIS", "MISSING"]

class ResearchPlanningProposal(TypedDict):
    schemaVersion: Literal["research-planning-proposal-v1"]
    organizationId: str
    runId: str
    contextHash: str
    sourceHash: str
    sourceCutoff: str
    subject: ResearchPlanningProposalSubject
    question: str
    status: Literal["NEEDS_INPUT", "NEEDS_REVIEW"]
    candidate: ResearchPlanningProposalCandidate
    missingInputs: list[Literal["objective", "baselineScenario", "seed", "stepCount", "startingPortfolioQuote", "startingDepthQuote", "startingInventoryPips"]]
    validationIssues: list[ResearchPlanningProposalValidationIssuesItem]
    unsupportedRequests: list[Literal["CALENDAR_TIME", "HISTORICAL_AS_OF", "ACTUAL_HOLDINGS_BASELINE", "EXACT_UNLOCK_TIMING", "POSITIVE_BUYER_IMPACT", "GAS_ABOVE_TWO_TIMES", "UNLOCK_MARKET_DEPTH_IMPACT", "FILL_ACCURATE_BACKTEST", "OTHER_UNSUPPORTED"]]
    provenance: list[ResearchPlanningProposalProvenanceItem]
    requiredAcknowledgements: list[Literal["MODELED_STEPS_NOT_CALENDAR_DAYS", "CURRENT_DATA_NOT_HISTORICAL_REPLAY", "CURRENT_IS_PLANNER_GENERATED_NOT_ACTUAL_HOLDINGS", "UNLOCKS_AGGREGATED_AT_MIDPOINT", "NO_POSITIVE_BUYER_PRICE_IMPACT", "GAS_INCREASE_AT_MOST_TWO_TIMES", "QUOTE_IDENTITY_AND_DECIMALS_UNVERIFIED", "SCENARIOS_ARE_HYPOTHESES_NOT_FORECASTS", "UNLOCK_MAGNITUDE_IS_WEIGHTED_PARTICIPATION_PROXY", "HISTORICAL_RETURNS_ARE_FIXED_RETURN_MODEL_REPLAY", "DRIVER_ATTRIBUTION_IS_APPROXIMATE", "RESERVE_ORACLE_BREACH_IS_COMPOSITE_MODELED_EVENT"]]
    financialAuthority: Literal[False]
    publicationAuthority: Literal[False]
    executionAuthorized: Literal[False]
    proposalHash: str

class ResearchPlanningConfirmation(TypedDict):
    proposalHash: str
    expectedSourceResourceVersion: str
    acceptedAcknowledgements: list[Literal["MODELED_STEPS_NOT_CALENDAR_DAYS", "CURRENT_DATA_NOT_HISTORICAL_REPLAY", "CURRENT_IS_PLANNER_GENERATED_NOT_ACTUAL_HOLDINGS", "UNLOCKS_AGGREGATED_AT_MIDPOINT", "NO_POSITIVE_BUYER_PRICE_IMPACT", "GAS_INCREASE_AT_MOST_TWO_TIMES", "QUOTE_IDENTITY_AND_DECIMALS_UNVERIFIED", "SCENARIOS_ARE_HYPOTHESES_NOT_FORECASTS", "UNLOCK_MAGNITUDE_IS_WEIGHTED_PARTICIPATION_PROXY", "HISTORICAL_RETURNS_ARE_FIXED_RETURN_MODEL_REPLAY", "DRIVER_ATTRIBUTION_IS_APPROXIMATE", "RESERVE_ORACLE_BREACH_IS_COMPOSITE_MODELED_EVENT"]]
    acceptProposedHypotheses: Literal[True]
    limitationsAccepted: Literal[True]

class ResearchComparisonObjective(TypedDict):
    metric: Literal["ENDING_VALUE_P50", "MINIMUM_DEPTH_P5", "GAS_COST_P50", "DRAWDOWN_P95", "RESERVE_BREACH_PROBABILITY"]
    direction: Literal["MAXIMIZE", "MINIMIZE"]

class ResearchComparisonContextVariant1(TypedDict):
    organizationId: str
    issuerIntentId: str
    issuerIntentResourceVersion: str
    issuerIntentArtifactHash: str
    sourceCutoff: str
    quoteSymbol: str
    quoteAssetId: Union[str, None]
    quoteDecimals: Union[int, None]
    seedPolicyVersion: str
    horizonUnit: Literal["MODELED_STEPS", "CALIBRATED_STEPS"]
    stepDurationSeconds: Union[int, None]
    analysisBasis: Literal["CURRENT_DATA_HYPOTHETICAL", "HISTORICAL_POINT_IN_TIME"]
    historicalAvailabilityEvidenceHash: Union[str, None]

class ResearchComparisonTrialsItemContextVariant1(TypedDict):
    organizationId: str
    issuerIntentId: str
    issuerIntentResourceVersion: str
    issuerIntentArtifactHash: str
    sourceCutoff: str
    quoteSymbol: str
    quoteAssetId: Union[str, None]
    quoteDecimals: Union[int, None]
    seedPolicyVersion: str
    horizonUnit: Literal["MODELED_STEPS", "CALIBRATED_STEPS"]
    stepDurationSeconds: Union[int, None]
    analysisBasis: Literal["CURRENT_DATA_HYPOTHETICAL", "HISTORICAL_POINT_IN_TIME"]
    historicalAvailabilityEvidenceHash: Union[str, None]

class ResearchComparisonTrialsItemAdmittedInputVariant1ScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchComparisonTrialsItemAdmittedInputVariant1Scenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchComparisonTrialsItemAdmittedInputVariant1ScenarioUnlocksItem]

class ResearchComparisonTrialsItemAdmittedInputVariant1VariantsItem(TypedDict):
    kind: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    requiredCapitalQuote: str
    deployableCapitalQuote: str
    stableReserveQuote: str
    emergencyReserveQuote: str
    rangeWidthPips: int
    expectedSlippagePips: int
    expectedFeeIncomeLowQuote: str
    expectedFeeIncomeHighQuote: str
    inventoryExposurePips: int
    maximumDailyTurnoverPips: int
    satisfiesIntent: bool
    reasons: list[str]

class ResearchComparisonTrialsItemAdmittedInputVariant1(TypedDict):
    schemaVersion: Literal["simulation-study-input-snapshot-v1"]
    engineVersion: Literal["digital-twin-pcg64-fixed-v2"]
    seed: str
    pathCount: Union[Literal[2000], Literal[10000]]
    stepCount: int
    targetTradeSizeQuote: str
    startingPortfolioQuote: str
    startingDepthQuote: str
    startingInventoryPips: int
    scenario: ResearchComparisonTrialsItemAdmittedInputVariant1Scenario
    variants: list[ResearchComparisonTrialsItemAdmittedInputVariant1VariantsItem]

class ResearchComparisonTrialsItemVariantsItemCapitalPlan(TypedDict):
    kind: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    requiredCapitalQuote: str
    deployableCapitalQuote: str
    stableReserveQuote: str
    emergencyReserveQuote: str
    rangeWidthPips: int
    expectedSlippagePips: int
    expectedFeeIncomeLowQuote: str
    expectedFeeIncomeHighQuote: str
    inventoryExposurePips: int
    maximumDailyTurnoverPips: int
    satisfiesIntent: bool
    reasons: list[str]

class ResearchComparisonTrialsItemVariantsItemOutcomesEndingValueQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchComparisonTrialsItemVariantsItemOutcomesTurnoverQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchComparisonTrialsItemVariantsItemOutcomesGasCostQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchComparisonTrialsItemVariantsItemOutcomesFeeIncomeQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchComparisonTrialsItemVariantsItemOutcomesProtocolFeesQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchComparisonTrialsItemVariantsItemOutcomesPlatformFeesQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchComparisonTrialsItemVariantsItemOutcomesMinimumDepthQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchComparisonTrialsItemVariantsItemOutcomesSlippagePips(TypedDict):
    p5: int
    p25: int
    p50: int
    p75: int
    p95: int

class ResearchComparisonTrialsItemVariantsItemOutcomesDrawdownPips(TypedDict):
    p5: int
    p25: int
    p50: int
    p75: int
    p95: int

class ResearchComparisonTrialsItemVariantsItemOutcomesInventoryPips(TypedDict):
    p5: int
    p25: int
    p50: int
    p75: int
    p95: int

class ResearchComparisonTrialsItemVariantsItemOutcomesDriversItem(TypedDict):
    driver: Literal["PRICE_PATH", "VOLATILITY", "FLOW", "LIQUIDITY", "UNLOCK", "GAS", "RESERVE"]
    impactQuote: str
    evidence: str
    method: Literal["DETERMINISTIC_COUNTERFACTUAL_DELTA_V1"]

class ResearchComparisonTrialsItemVariantsItemOutcomes(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    endingValueQuote: ResearchComparisonTrialsItemVariantsItemOutcomesEndingValueQuote
    turnoverQuote: ResearchComparisonTrialsItemVariantsItemOutcomesTurnoverQuote
    gasCostQuote: ResearchComparisonTrialsItemVariantsItemOutcomesGasCostQuote
    feeIncomeQuote: ResearchComparisonTrialsItemVariantsItemOutcomesFeeIncomeQuote
    protocolFeesQuote: ResearchComparisonTrialsItemVariantsItemOutcomesProtocolFeesQuote
    platformFeesQuote: ResearchComparisonTrialsItemVariantsItemOutcomesPlatformFeesQuote
    minimumDepthQuote: ResearchComparisonTrialsItemVariantsItemOutcomesMinimumDepthQuote
    slippagePips: ResearchComparisonTrialsItemVariantsItemOutcomesSlippagePips
    drawdownPips: ResearchComparisonTrialsItemVariantsItemOutcomesDrawdownPips
    inventoryPips: ResearchComparisonTrialsItemVariantsItemOutcomesInventoryPips
    reserveBreachProbabilityPips: int
    drivers: list[ResearchComparisonTrialsItemVariantsItemOutcomesDriversItem]

class ResearchComparisonTrialsItemVariantsItemDifferencesItem(TypedDict):
    metric: Literal["endingValueQuote", "turnoverQuote", "gasCostQuote", "feeIncomeQuote", "protocolFeesQuote", "platformFeesQuote", "minimumDepthQuote", "slippagePips", "drawdownPips", "inventoryPips", "reserveBreachProbabilityPips"]
    percentile: Union[Literal["p5", "p25", "p50", "p75", "p95"], None]
    unit: Literal["VERIFIED_QUOTE_ASSET_ATOMIC", "ISSUER_INTENT_QUOTE_ATOMIC", "PIPS_POINT_DIFFERENCE"]
    baseline: str
    scenario: str
    delta: str
    interpretation: Literal["DIFFERENCE_OF_MARGINAL_PERCENTILES", "DIFFERENCE_OF_PROBABILITIES"]

class ResearchComparisonTrialsItemVariantsItem(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    capitalPlan: ResearchComparisonTrialsItemVariantsItemCapitalPlan
    outcomes: ResearchComparisonTrialsItemVariantsItemOutcomes
    eligible: bool
    ineligibilityReasons: list[str]
    differences: list[ResearchComparisonTrialsItemVariantsItemDifferencesItem]

class ResearchComparisonTrialsItemRankingEntriesItem(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    rank: int
    objectiveValue: str

class ResearchComparisonTrialsItemRanking(TypedDict):
    status: Literal["BLOCKED", "NO_ELIGIBLE_RECOMMENDATION", "RANKED"]
    reason: Union[str, None]
    entries: list[ResearchComparisonTrialsItemRankingEntriesItem]

class ResearchComparisonTrialsItem(TypedDict):
    trialId: str
    label: str
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    failureCode: Union[str, None]
    admittedInputHash: Union[str, None]
    resultArtifactHash: Union[str, None]
    context: Union[ResearchComparisonTrialsItemContextVariant1, None]
    admittedInput: Union[ResearchComparisonTrialsItemAdmittedInputVariant1, None]
    status: Literal["PENDING", "FAILED", "CANCELLED", "INVALID", "INCOMPATIBLE", "BASELINE_UNAVAILABLE", "COMPARABLE"]
    reasons: list[str]
    warnings: list[str]
    variants: list[ResearchComparisonTrialsItemVariantsItem]
    ranking: ResearchComparisonTrialsItemRanking

class ResearchComparison(TypedDict):
    schemaVersion: Literal["research-comparison-v1"]
    baselineTrialId: str
    objective: ResearchComparisonObjective
    context: Union[ResearchComparisonContextVariant1, None]
    status: Literal["BASELINE_UNAVAILABLE", "COMPLETE", "PARTIAL"]
    eligibilityRule: Literal["ADMITTED_INTENT_CONSTRAINTS_AND_RESERVE_BREACH_AT_MOST_100000_PIPS"]
    rankingScope: Literal["WITHIN_SCENARIO_VARIANTS"]
    limitations: list[Literal["CURRENT_IS_ENGINE_GENERATED_NOT_ACTUAL_HOLDINGS", "COMPARISON_DOES_NOT_PROVE_EQUAL_CAPITAL_SUPERIORITY", "MARGINAL_PERCENTILE_DIFFERENCES_ARE_NOT_PAIRED_DIFFERENCE_PERCENTILES", "RESERVE_BREACH_IS_COMPOSITE_RESERVE_OR_ORACLE_BLOCKED_EVENT", "MODEL_OUTCOMES_ARE_NOT_FINANCIAL_GUARANTEES", "ARTIFACT_HASHES_DO_NOT_REPRODUCE_ENGINE_OUTPUT"]]
    trials: list[ResearchComparisonTrialsItem]

class ResearchReportComparisonObjective(TypedDict):
    metric: Literal["ENDING_VALUE_P50", "MINIMUM_DEPTH_P5", "GAS_COST_P50", "DRAWDOWN_P95", "RESERVE_BREACH_PROBABILITY"]
    direction: Literal["MAXIMIZE", "MINIMIZE"]

class ResearchReportComparisonContextVariant1(TypedDict):
    organizationId: str
    issuerIntentId: str
    issuerIntentResourceVersion: str
    issuerIntentArtifactHash: str
    sourceCutoff: str
    quoteSymbol: str
    quoteAssetId: Union[str, None]
    quoteDecimals: Union[int, None]
    seedPolicyVersion: str
    horizonUnit: Literal["MODELED_STEPS", "CALIBRATED_STEPS"]
    stepDurationSeconds: Union[int, None]
    analysisBasis: Literal["CURRENT_DATA_HYPOTHETICAL", "HISTORICAL_POINT_IN_TIME"]
    historicalAvailabilityEvidenceHash: Union[str, None]

class ResearchReportComparisonTrialsItemContextVariant1(TypedDict):
    organizationId: str
    issuerIntentId: str
    issuerIntentResourceVersion: str
    issuerIntentArtifactHash: str
    sourceCutoff: str
    quoteSymbol: str
    quoteAssetId: Union[str, None]
    quoteDecimals: Union[int, None]
    seedPolicyVersion: str
    horizonUnit: Literal["MODELED_STEPS", "CALIBRATED_STEPS"]
    stepDurationSeconds: Union[int, None]
    analysisBasis: Literal["CURRENT_DATA_HYPOTHETICAL", "HISTORICAL_POINT_IN_TIME"]
    historicalAvailabilityEvidenceHash: Union[str, None]

class ResearchReportComparisonTrialsItemAdmittedInputVariant1ScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchReportComparisonTrialsItemAdmittedInputVariant1Scenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchReportComparisonTrialsItemAdmittedInputVariant1ScenarioUnlocksItem]

class ResearchReportComparisonTrialsItemAdmittedInputVariant1VariantsItem(TypedDict):
    kind: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    requiredCapitalQuote: str
    deployableCapitalQuote: str
    stableReserveQuote: str
    emergencyReserveQuote: str
    rangeWidthPips: int
    expectedSlippagePips: int
    expectedFeeIncomeLowQuote: str
    expectedFeeIncomeHighQuote: str
    inventoryExposurePips: int
    maximumDailyTurnoverPips: int
    satisfiesIntent: bool
    reasons: list[str]

class ResearchReportComparisonTrialsItemAdmittedInputVariant1(TypedDict):
    schemaVersion: Literal["simulation-study-input-snapshot-v1"]
    engineVersion: Literal["digital-twin-pcg64-fixed-v2"]
    seed: str
    pathCount: Union[Literal[2000], Literal[10000]]
    stepCount: int
    targetTradeSizeQuote: str
    startingPortfolioQuote: str
    startingDepthQuote: str
    startingInventoryPips: int
    scenario: ResearchReportComparisonTrialsItemAdmittedInputVariant1Scenario
    variants: list[ResearchReportComparisonTrialsItemAdmittedInputVariant1VariantsItem]

class ResearchReportComparisonTrialsItemVariantsItemCapitalPlan(TypedDict):
    kind: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    requiredCapitalQuote: str
    deployableCapitalQuote: str
    stableReserveQuote: str
    emergencyReserveQuote: str
    rangeWidthPips: int
    expectedSlippagePips: int
    expectedFeeIncomeLowQuote: str
    expectedFeeIncomeHighQuote: str
    inventoryExposurePips: int
    maximumDailyTurnoverPips: int
    satisfiesIntent: bool
    reasons: list[str]

class ResearchReportComparisonTrialsItemVariantsItemOutcomesEndingValueQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchReportComparisonTrialsItemVariantsItemOutcomesTurnoverQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchReportComparisonTrialsItemVariantsItemOutcomesGasCostQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchReportComparisonTrialsItemVariantsItemOutcomesFeeIncomeQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchReportComparisonTrialsItemVariantsItemOutcomesProtocolFeesQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchReportComparisonTrialsItemVariantsItemOutcomesPlatformFeesQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchReportComparisonTrialsItemVariantsItemOutcomesMinimumDepthQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class ResearchReportComparisonTrialsItemVariantsItemOutcomesSlippagePips(TypedDict):
    p5: int
    p25: int
    p50: int
    p75: int
    p95: int

class ResearchReportComparisonTrialsItemVariantsItemOutcomesDrawdownPips(TypedDict):
    p5: int
    p25: int
    p50: int
    p75: int
    p95: int

class ResearchReportComparisonTrialsItemVariantsItemOutcomesInventoryPips(TypedDict):
    p5: int
    p25: int
    p50: int
    p75: int
    p95: int

class ResearchReportComparisonTrialsItemVariantsItemOutcomesDriversItem(TypedDict):
    driver: Literal["PRICE_PATH", "VOLATILITY", "FLOW", "LIQUIDITY", "UNLOCK", "GAS", "RESERVE"]
    impactQuote: str
    evidence: str
    method: Literal["DETERMINISTIC_COUNTERFACTUAL_DELTA_V1"]

class ResearchReportComparisonTrialsItemVariantsItemOutcomes(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    endingValueQuote: ResearchReportComparisonTrialsItemVariantsItemOutcomesEndingValueQuote
    turnoverQuote: ResearchReportComparisonTrialsItemVariantsItemOutcomesTurnoverQuote
    gasCostQuote: ResearchReportComparisonTrialsItemVariantsItemOutcomesGasCostQuote
    feeIncomeQuote: ResearchReportComparisonTrialsItemVariantsItemOutcomesFeeIncomeQuote
    protocolFeesQuote: ResearchReportComparisonTrialsItemVariantsItemOutcomesProtocolFeesQuote
    platformFeesQuote: ResearchReportComparisonTrialsItemVariantsItemOutcomesPlatformFeesQuote
    minimumDepthQuote: ResearchReportComparisonTrialsItemVariantsItemOutcomesMinimumDepthQuote
    slippagePips: ResearchReportComparisonTrialsItemVariantsItemOutcomesSlippagePips
    drawdownPips: ResearchReportComparisonTrialsItemVariantsItemOutcomesDrawdownPips
    inventoryPips: ResearchReportComparisonTrialsItemVariantsItemOutcomesInventoryPips
    reserveBreachProbabilityPips: int
    drivers: list[ResearchReportComparisonTrialsItemVariantsItemOutcomesDriversItem]

class ResearchReportComparisonTrialsItemVariantsItemDifferencesItem(TypedDict):
    metric: Literal["endingValueQuote", "turnoverQuote", "gasCostQuote", "feeIncomeQuote", "protocolFeesQuote", "platformFeesQuote", "minimumDepthQuote", "slippagePips", "drawdownPips", "inventoryPips", "reserveBreachProbabilityPips"]
    percentile: Union[Literal["p5", "p25", "p50", "p75", "p95"], None]
    unit: Literal["VERIFIED_QUOTE_ASSET_ATOMIC", "ISSUER_INTENT_QUOTE_ATOMIC", "PIPS_POINT_DIFFERENCE"]
    baseline: str
    scenario: str
    delta: str
    interpretation: Literal["DIFFERENCE_OF_MARGINAL_PERCENTILES", "DIFFERENCE_OF_PROBABILITIES"]

class ResearchReportComparisonTrialsItemVariantsItem(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    capitalPlan: ResearchReportComparisonTrialsItemVariantsItemCapitalPlan
    outcomes: ResearchReportComparisonTrialsItemVariantsItemOutcomes
    eligible: bool
    ineligibilityReasons: list[str]
    differences: list[ResearchReportComparisonTrialsItemVariantsItemDifferencesItem]

class ResearchReportComparisonTrialsItemRankingEntriesItem(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    rank: int
    objectiveValue: str

class ResearchReportComparisonTrialsItemRanking(TypedDict):
    status: Literal["BLOCKED", "NO_ELIGIBLE_RECOMMENDATION", "RANKED"]
    reason: Union[str, None]
    entries: list[ResearchReportComparisonTrialsItemRankingEntriesItem]

class ResearchReportComparisonTrialsItem(TypedDict):
    trialId: str
    label: str
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    failureCode: Union[str, None]
    admittedInputHash: Union[str, None]
    resultArtifactHash: Union[str, None]
    context: Union[ResearchReportComparisonTrialsItemContextVariant1, None]
    admittedInput: Union[ResearchReportComparisonTrialsItemAdmittedInputVariant1, None]
    status: Literal["PENDING", "FAILED", "CANCELLED", "INVALID", "INCOMPATIBLE", "BASELINE_UNAVAILABLE", "COMPARABLE"]
    reasons: list[str]
    warnings: list[str]
    variants: list[ResearchReportComparisonTrialsItemVariantsItem]
    ranking: ResearchReportComparisonTrialsItemRanking

class ResearchReportComparison(TypedDict):
    schemaVersion: Literal["research-comparison-v1"]
    baselineTrialId: str
    objective: ResearchReportComparisonObjective
    context: Union[ResearchReportComparisonContextVariant1, None]
    status: Literal["BASELINE_UNAVAILABLE", "COMPLETE", "PARTIAL"]
    eligibilityRule: Literal["ADMITTED_INTENT_CONSTRAINTS_AND_RESERVE_BREACH_AT_MOST_100000_PIPS"]
    rankingScope: Literal["WITHIN_SCENARIO_VARIANTS"]
    limitations: list[Literal["CURRENT_IS_ENGINE_GENERATED_NOT_ACTUAL_HOLDINGS", "COMPARISON_DOES_NOT_PROVE_EQUAL_CAPITAL_SUPERIORITY", "MARGINAL_PERCENTILE_DIFFERENCES_ARE_NOT_PAIRED_DIFFERENCE_PERCENTILES", "RESERVE_BREACH_IS_COMPOSITE_RESERVE_OR_ORACLE_BLOCKED_EVENT", "MODEL_OUTCOMES_ARE_NOT_FINANCIAL_GUARANTEES", "ARTIFACT_HASHES_DO_NOT_REPRODUCE_ENGINE_OUTPUT"]]
    trials: list[ResearchReportComparisonTrialsItem]

class ResearchReportFindingsItem(TypedDict):
    id: str
    kind: Literal["SCOPE", "ANALYSIS_BASIS", "DISPOSITION", "TRIAL", "ELIGIBILITY", "ADVERSE_OUTCOME", "LIMITATION", "METRIC_EXPLANATION"]
    mandatory: bool
    severity: Literal["INFO", "WARNING"]
    summary: str
    trialId: Union[str, None]

class ResearchReport(TypedDict):
    schemaVersion: Literal["agent-research-report-v1"]
    organizationId: str
    runId: str
    protocolHash: str
    sourceCutoff: str
    status: Literal["ABSTAINED", "PARTIAL", "COMPLETED"]
    comparison: ResearchReportComparison
    findings: list[ResearchReportFindingsItem]
    nextChecks: list[Literal["INSPECT_STUDY_INPUTS", "INSPECT_FAILED_TRIALS", "REVIEW_MODEL_LIMITATIONS", "EDIT_AND_RERUN", "RETURN_TO_PLAN"]]
    financialAuthority: Literal[False]
    publicationAuthority: Literal[False]

class SavedResearchResultReportComparisonObjective(TypedDict):
    metric: Literal["ENDING_VALUE_P50", "MINIMUM_DEPTH_P5", "GAS_COST_P50", "DRAWDOWN_P95", "RESERVE_BREACH_PROBABILITY"]
    direction: Literal["MAXIMIZE", "MINIMIZE"]

class SavedResearchResultReportComparisonContextVariant1(TypedDict):
    organizationId: str
    issuerIntentId: str
    issuerIntentResourceVersion: str
    issuerIntentArtifactHash: str
    sourceCutoff: str
    quoteSymbol: str
    quoteAssetId: Union[str, None]
    quoteDecimals: Union[int, None]
    seedPolicyVersion: str
    horizonUnit: Literal["MODELED_STEPS", "CALIBRATED_STEPS"]
    stepDurationSeconds: Union[int, None]
    analysisBasis: Literal["CURRENT_DATA_HYPOTHETICAL", "HISTORICAL_POINT_IN_TIME"]
    historicalAvailabilityEvidenceHash: Union[str, None]

class SavedResearchResultReportComparisonTrialsItemContextVariant1(TypedDict):
    organizationId: str
    issuerIntentId: str
    issuerIntentResourceVersion: str
    issuerIntentArtifactHash: str
    sourceCutoff: str
    quoteSymbol: str
    quoteAssetId: Union[str, None]
    quoteDecimals: Union[int, None]
    seedPolicyVersion: str
    horizonUnit: Literal["MODELED_STEPS", "CALIBRATED_STEPS"]
    stepDurationSeconds: Union[int, None]
    analysisBasis: Literal["CURRENT_DATA_HYPOTHETICAL", "HISTORICAL_POINT_IN_TIME"]
    historicalAvailabilityEvidenceHash: Union[str, None]

class SavedResearchResultReportComparisonTrialsItemAdmittedInputVariant1ScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class SavedResearchResultReportComparisonTrialsItemAdmittedInputVariant1Scenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[SavedResearchResultReportComparisonTrialsItemAdmittedInputVariant1ScenarioUnlocksItem]

class SavedResearchResultReportComparisonTrialsItemAdmittedInputVariant1VariantsItem(TypedDict):
    kind: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    requiredCapitalQuote: str
    deployableCapitalQuote: str
    stableReserveQuote: str
    emergencyReserveQuote: str
    rangeWidthPips: int
    expectedSlippagePips: int
    expectedFeeIncomeLowQuote: str
    expectedFeeIncomeHighQuote: str
    inventoryExposurePips: int
    maximumDailyTurnoverPips: int
    satisfiesIntent: bool
    reasons: list[str]

class SavedResearchResultReportComparisonTrialsItemAdmittedInputVariant1(TypedDict):
    schemaVersion: Literal["simulation-study-input-snapshot-v1"]
    engineVersion: Literal["digital-twin-pcg64-fixed-v2"]
    seed: str
    pathCount: Union[Literal[2000], Literal[10000]]
    stepCount: int
    targetTradeSizeQuote: str
    startingPortfolioQuote: str
    startingDepthQuote: str
    startingInventoryPips: int
    scenario: SavedResearchResultReportComparisonTrialsItemAdmittedInputVariant1Scenario
    variants: list[SavedResearchResultReportComparisonTrialsItemAdmittedInputVariant1VariantsItem]

class SavedResearchResultReportComparisonTrialsItemVariantsItemCapitalPlan(TypedDict):
    kind: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    requiredCapitalQuote: str
    deployableCapitalQuote: str
    stableReserveQuote: str
    emergencyReserveQuote: str
    rangeWidthPips: int
    expectedSlippagePips: int
    expectedFeeIncomeLowQuote: str
    expectedFeeIncomeHighQuote: str
    inventoryExposurePips: int
    maximumDailyTurnoverPips: int
    satisfiesIntent: bool
    reasons: list[str]

class SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesEndingValueQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesTurnoverQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesGasCostQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesFeeIncomeQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesProtocolFeesQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesPlatformFeesQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesMinimumDepthQuote(TypedDict):
    p5: str
    p25: str
    p50: str
    p75: str
    p95: str

class SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesSlippagePips(TypedDict):
    p5: int
    p25: int
    p50: int
    p75: int
    p95: int

class SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesDrawdownPips(TypedDict):
    p5: int
    p25: int
    p50: int
    p75: int
    p95: int

class SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesInventoryPips(TypedDict):
    p5: int
    p25: int
    p50: int
    p75: int
    p95: int

class SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesDriversItem(TypedDict):
    driver: Literal["PRICE_PATH", "VOLATILITY", "FLOW", "LIQUIDITY", "UNLOCK", "GAS", "RESERVE"]
    impactQuote: str
    evidence: str
    method: Literal["DETERMINISTIC_COUNTERFACTUAL_DELTA_V1"]

class SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomes(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    endingValueQuote: SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesEndingValueQuote
    turnoverQuote: SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesTurnoverQuote
    gasCostQuote: SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesGasCostQuote
    feeIncomeQuote: SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesFeeIncomeQuote
    protocolFeesQuote: SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesProtocolFeesQuote
    platformFeesQuote: SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesPlatformFeesQuote
    minimumDepthQuote: SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesMinimumDepthQuote
    slippagePips: SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesSlippagePips
    drawdownPips: SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesDrawdownPips
    inventoryPips: SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesInventoryPips
    reserveBreachProbabilityPips: int
    drivers: list[SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomesDriversItem]

class SavedResearchResultReportComparisonTrialsItemVariantsItemDifferencesItem(TypedDict):
    metric: Literal["endingValueQuote", "turnoverQuote", "gasCostQuote", "feeIncomeQuote", "protocolFeesQuote", "platformFeesQuote", "minimumDepthQuote", "slippagePips", "drawdownPips", "inventoryPips", "reserveBreachProbabilityPips"]
    percentile: Union[Literal["p5", "p25", "p50", "p75", "p95"], None]
    unit: Literal["VERIFIED_QUOTE_ASSET_ATOMIC", "ISSUER_INTENT_QUOTE_ATOMIC", "PIPS_POINT_DIFFERENCE"]
    baseline: str
    scenario: str
    delta: str
    interpretation: Literal["DIFFERENCE_OF_MARGINAL_PERCENTILES", "DIFFERENCE_OF_PROBABILITIES"]

class SavedResearchResultReportComparisonTrialsItemVariantsItem(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    capitalPlan: SavedResearchResultReportComparisonTrialsItemVariantsItemCapitalPlan
    outcomes: SavedResearchResultReportComparisonTrialsItemVariantsItemOutcomes
    eligible: bool
    ineligibilityReasons: list[str]
    differences: list[SavedResearchResultReportComparisonTrialsItemVariantsItemDifferencesItem]

class SavedResearchResultReportComparisonTrialsItemRankingEntriesItem(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    rank: int
    objectiveValue: str

class SavedResearchResultReportComparisonTrialsItemRanking(TypedDict):
    status: Literal["BLOCKED", "NO_ELIGIBLE_RECOMMENDATION", "RANKED"]
    reason: Union[str, None]
    entries: list[SavedResearchResultReportComparisonTrialsItemRankingEntriesItem]

class SavedResearchResultReportComparisonTrialsItem(TypedDict):
    trialId: str
    label: str
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    failureCode: Union[str, None]
    admittedInputHash: Union[str, None]
    resultArtifactHash: Union[str, None]
    context: Union[SavedResearchResultReportComparisonTrialsItemContextVariant1, None]
    admittedInput: Union[SavedResearchResultReportComparisonTrialsItemAdmittedInputVariant1, None]
    status: Literal["PENDING", "FAILED", "CANCELLED", "INVALID", "INCOMPATIBLE", "BASELINE_UNAVAILABLE", "COMPARABLE"]
    reasons: list[str]
    warnings: list[str]
    variants: list[SavedResearchResultReportComparisonTrialsItemVariantsItem]
    ranking: SavedResearchResultReportComparisonTrialsItemRanking

class SavedResearchResultReportComparison(TypedDict):
    schemaVersion: Literal["research-comparison-v1"]
    baselineTrialId: str
    objective: SavedResearchResultReportComparisonObjective
    context: Union[SavedResearchResultReportComparisonContextVariant1, None]
    status: Literal["BASELINE_UNAVAILABLE", "COMPLETE", "PARTIAL"]
    eligibilityRule: Literal["ADMITTED_INTENT_CONSTRAINTS_AND_RESERVE_BREACH_AT_MOST_100000_PIPS"]
    rankingScope: Literal["WITHIN_SCENARIO_VARIANTS"]
    limitations: list[Literal["CURRENT_IS_ENGINE_GENERATED_NOT_ACTUAL_HOLDINGS", "COMPARISON_DOES_NOT_PROVE_EQUAL_CAPITAL_SUPERIORITY", "MARGINAL_PERCENTILE_DIFFERENCES_ARE_NOT_PAIRED_DIFFERENCE_PERCENTILES", "RESERVE_BREACH_IS_COMPOSITE_RESERVE_OR_ORACLE_BLOCKED_EVENT", "MODEL_OUTCOMES_ARE_NOT_FINANCIAL_GUARANTEES", "ARTIFACT_HASHES_DO_NOT_REPRODUCE_ENGINE_OUTPUT"]]
    trials: list[SavedResearchResultReportComparisonTrialsItem]

class SavedResearchResultReportFindingsItem(TypedDict):
    id: str
    kind: Literal["SCOPE", "ANALYSIS_BASIS", "DISPOSITION", "TRIAL", "ELIGIBILITY", "ADVERSE_OUTCOME", "LIMITATION", "METRIC_EXPLANATION"]
    mandatory: bool
    severity: Literal["INFO", "WARNING"]
    summary: str
    trialId: Union[str, None]

class SavedResearchResultReport(TypedDict):
    schemaVersion: Literal["agent-research-report-v1"]
    organizationId: str
    runId: str
    protocolHash: str
    sourceCutoff: str
    status: Literal["ABSTAINED", "PARTIAL", "COMPLETED"]
    comparison: SavedResearchResultReportComparison
    findings: list[SavedResearchResultReportFindingsItem]
    nextChecks: list[Literal["INSPECT_STUDY_INPUTS", "INSPECT_FAILED_TRIALS", "REVIEW_MODEL_LIMITATIONS", "EDIT_AND_RERUN", "RETURN_TO_PLAN"]]
    financialAuthority: Literal[False]
    publicationAuthority: Literal[False]

class SavedResearchResultApplicability(TypedDict):
    scope: Literal["ISSUER_INTENT_VERSION_ONLY"]
    status: Literal["SAME_SUBJECT_VERSION", "SUBJECT_CHANGED", "SUBJECT_UNAVAILABLE"]
    checkedAt: str
    savedSubjectVersion: str
    currentSubjectVersion: Union[str, None]

class SavedResearchResult(TypedDict):
    schemaVersion: Literal["saved-research-result-v1"]
    organizationId: str
    runId: str
    resultVersion: str
    completedAt: str
    protocolHash: str
    report: SavedResearchResultReport
    applicability: SavedResearchResultApplicability

class ResearchTrialInputInputScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchTrialInputInputScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchTrialInputInputScenarioUnlocksItem]

class ResearchTrialInputInputVariantsItem(TypedDict):
    kind: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    requiredCapitalQuote: str
    deployableCapitalQuote: str
    stableReserveQuote: str
    emergencyReserveQuote: str
    rangeWidthPips: int
    expectedSlippagePips: int
    expectedFeeIncomeLowQuote: str
    expectedFeeIncomeHighQuote: str
    inventoryExposurePips: int
    maximumDailyTurnoverPips: int
    satisfiesIntent: bool
    reasons: list[str]

class ResearchTrialInputInput(TypedDict):
    seed: str
    pathCount: Union[Literal[2000], Literal[10000]]
    stepCount: int
    targetTradeSizeQuote: str
    startingPortfolioQuote: str
    startingDepthQuote: str
    startingInventoryPips: int
    scenario: ResearchTrialInputInputScenario
    variants: list[ResearchTrialInputInputVariantsItem]

class ResearchTrialInput(TypedDict):
    schemaVersion: Literal["agent-research-trial-input-v1"]
    organizationId: str
    runId: str
    trialKey: Literal["baseline", "alternative-1", "alternative-2", "alternative-3"]
    label: str
    protocolHash: str
    inputHash: str
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    chargedComputeUnits: str
    failureCode: Union[str, None]
    artifactHash: Union[str, None]
    recordedAt: Union[str, None]
    input: ResearchTrialInputInput
    financialAuthority: Literal[False]
    publicationAuthority: Literal[False]

class ResearchAdmissionRequestSubject(TypedDict):
    issuerIntentId: str
    expectedResourceVersion: str

class ResearchAdmissionRequestExperimentObjective(TypedDict):
    metric: Literal["ENDING_VALUE_P50", "MINIMUM_DEPTH_P5", "GAS_COST_P50", "DRAWDOWN_P95", "RESERVE_BREACH_PROBABILITY"]
    direction: Literal["MAXIMIZE", "MINIMIZE"]

class ResearchAdmissionRequestExperimentBaselineScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchAdmissionRequestExperimentBaselineScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchAdmissionRequestExperimentBaselineScenarioUnlocksItem]

class ResearchAdmissionRequestExperimentAlternativesItemScenarioUnlocksItem(TypedDict):
    id: str
    unlocksAt: str
    tokenAmount: str
    recipientCategory: Literal["TEAM", "INVESTOR", "COMMUNITY", "TREASURY", "ECOSYSTEM", "OTHER"]
    expectedSaleParticipationPips: int
    confidencePips: int
    correlationGroup: NotRequired[str]
    evidenceHash: NotRequired[str]

class ResearchAdmissionRequestExperimentAlternativesItemScenario(TypedDict):
    id: str
    name: str
    kind: Literal["HISTORICAL_REPLAY", "BULL", "BEAR", "SIDEWAYS", "LIQUIDITY_CRISIS", "TOKEN_UNLOCK", "LARGE_BUYER", "LARGE_SELLER", "LIQUIDITY_WITHDRAWAL", "GAS_SPIKE", "ORACLE_OUTAGE", "COMBINED"]
    driftPipsPerStep: int
    volatilityPipsPerStep: int
    liquidityWithdrawalPips: int
    oneSidedFlowPips: int
    gasIncreasePips: int
    oracleOutageStep: NotRequired[int]
    historicalReturnPips: NotRequired[list[int]]
    protocolFeePips: NotRequired[int]
    platformFeePips: NotRequired[int]
    unlocks: list[ResearchAdmissionRequestExperimentAlternativesItemScenarioUnlocksItem]

class ResearchAdmissionRequestExperimentAlternativesItem(TypedDict):
    label: str
    scenario: ResearchAdmissionRequestExperimentAlternativesItemScenario

class ResearchAdmissionRequestExperiment(TypedDict):
    schemaVersion: Literal["research-experiment-v1"]
    objective: ResearchAdmissionRequestExperimentObjective
    seed: str
    pathCount: Literal[2000]
    stepCount: int
    startingPortfolioQuote: str
    startingDepthQuote: str
    startingInventoryPips: int
    baselineScenario: ResearchAdmissionRequestExperimentBaselineScenario
    alternatives: list[ResearchAdmissionRequestExperimentAlternativesItem]
    interpretation: Literal["CURRENT_DATA_HYPOTHETICAL_MODELED_STEPS"]
    limitationsAccepted: Literal[True]

class ResearchAdmissionRequest(TypedDict):
    kind: Literal["WHAT_IF_RESEARCH"]
    question: str
    subject: ResearchAdmissionRequestSubject
    experiment: ResearchAdmissionRequestExperiment

class ResearchProgressTrialsItem(TypedDict):
    trialKey: Literal["baseline", "alternative-1", "alternative-2", "alternative-3"]
    label: str
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    chargedComputeUnits: str
    failureCode: Union[str, None]
    artifactHash: Union[str, None]
    recordedAt: Union[str, None]
    inputHash: str

class ResearchProgress(TypedDict):
    schemaVersion: Literal["agent-research-progress-v1"]
    organizationId: str
    runId: str
    runResourceVersion: str
    runState: Literal["QUEUED", "RUNNING", "WAITING_FOR_INPUT", "WAITING_FOR_CHILDREN", "COMPLETED", "PARTIAL", "ABSTAINED", "FAILED", "CANCELLED"]
    checkedAt: str
    sourceCutoff: str
    protocolHash: Union[str, None]
    studyCount: Union[int, None]
    trials: list[ResearchProgressTrialsItem]
    financialAuthority: Literal[False]
    publicationAuthority: Literal[False]

class HealthAgentAdmissionRequestSubjectVariant1Window(TypedDict):
    start: str
    end: str

class HealthAgentAdmissionRequestSubjectVariant1BaselineWindow(TypedDict):
    start: str
    end: str

class HealthAgentAdmissionRequestSubjectVariant1(TypedDict):
    vaultId: str
    expectedVaultUpdatedAt: str
    window: HealthAgentAdmissionRequestSubjectVariant1Window
    baselineWindow: HealthAgentAdmissionRequestSubjectVariant1BaselineWindow

class HealthAgentAdmissionRequestSubjectVariant2(TypedDict):
    type: Literal["SAVED_PUBLIC_PROJECT"]
    projectId: str
    expectedResourceVersion: str
    observationSequence: str
    baselineSequence: Union[str, None]

class HealthAgentAdmissionRequest(TypedDict):
    kind: Literal["HEALTH_INVESTIGATION"]
    question: str
    subject: Union[HealthAgentAdmissionRequestSubjectVariant1, HealthAgentAdmissionRequestSubjectVariant2]

class ProposalReviewAdmissionRequestSubjectVariant1(TypedDict):
    generation: Literal["V1"]
    proposalId: str
    expectedUpdatedAt: str

class ProposalReviewAdmissionRequestSubjectVariant2(TypedDict):
    generation: Literal["V2"]
    proposalId: str
    expectedResourceVersion: str

class ProposalReviewAdmissionRequestSubjectVariant3(TypedDict):
    generation: Literal["DECISION_PACK"]
    packId: str
    expectedResourceVersion: str
    expectedContentHash: str

class ProposalReviewAdmissionRequest(TypedDict):
    kind: Literal["PROPOSAL_REVIEW"]
    question: str
    subject: Union[ProposalReviewAdmissionRequestSubjectVariant1, ProposalReviewAdmissionRequestSubjectVariant2, ProposalReviewAdmissionRequestSubjectVariant3]

AgentAdmissionRequest: TypeAlias = Union[HealthAgentAdmissionRequest, ProposalReviewAdmissionRequest, ResearchAdmissionRequest, ResearchPlanningAdmissionRequest]

class AgentAdmissionReceipt(TypedDict):
    schemaVersion: Literal["agent-admission-receipt-v1"]
    organizationId: str
    runId: str
    kind: Literal["HEALTH_INVESTIGATION", "PROPOSAL_REVIEW", "WHAT_IF_RESEARCH"]
    state: Literal["QUEUED", "RUNNING", "WAITING_FOR_INPUT", "WAITING_FOR_CHILDREN", "COMPLETED", "PARTIAL", "ABSTAINED", "FAILED", "CANCELLED"]
    phase: Literal["ADMITTED", "CAPTURING_EVIDENCE", "CHECKING_SOURCES", "COMPARING_EVIDENCE", "PLANNING", "READING_EVIDENCE", "WAITING_FOR_INPUT", "WAITING_FOR_STUDIES", "VALIDATING_REPORT", "FINISHED"]
    resourceVersion: str
    createdAt: str
    deadline: str
    replayed: bool

class HealthEvidenceSourceVariant1(TypedDict):
    generation: Literal["V1"]
    recordType: str
    recordId: str
    updatedAt: str
    copiedPayloadHash: str

class HealthEvidenceSourceVariant2(TypedDict):
    generation: Literal["V2"]
    recordType: str
    recordId: str
    resourceVersion: str
    artifactHash: str

HealthEvidenceSource: TypeAlias = Union[HealthEvidenceSourceVariant1, HealthEvidenceSourceVariant2]

class HealthFieldReceipt(TypedDict):
    evidenceId: str
    source: HealthEvidenceSource
    temporalScope: Literal["HISTORICAL", "CURRENT_CONTEXT"]
    observedAt: Union[str, None]
    availableAt: Union[str, None]
    capturedAt: str
    sourceCutoff: str
    quoteAssetId: Union[str, None]
    finality: Literal["FINALIZED", "NOT_APPLICABLE", "UNKNOWN"]
    field: str
    value: Union[str, int, bool]

class HealthMetricReading(TypedDict):
    evidenceId: str
    field: str
    value: str
    observedAt: str
    quoteAssetId: str
    quoteDecimals: int
    definition: str

class HealthMetricComparisonRelativeChangeVariant1(TypedDict):
    numerator: str
    denominator: str

class HealthMetricComparison(TypedDict):
    metric: Literal["QUOTE_BALANCE", "PROTECTED_QUOTE_RESERVE", "BUY_DEPTH", "SELL_DEPTH"]
    aggregation: Literal["LAST_RECORDED_SAMPLE"]
    unit: Literal["QUOTE_ATOMIC"]
    baseline: Union[HealthMetricReading, None]
    observation: Union[HealthMetricReading, None]
    status: Literal["COMPARABLE", "BASELINE_UNAVAILABLE", "OBSERVATION_UNAVAILABLE", "BOTH_UNAVAILABLE", "INCOMPATIBLE_UNITS", "INCOMPATIBLE_DEFINITION"]
    absoluteDelta: Union[str, None]
    relativeChange: Union[HealthMetricComparisonRelativeChangeVariant1, None]
    relativeUnavailableReason: Union[Literal["ZERO_BASELINE", "NOT_COMPARABLE"], None]

class HealthMarketQualityCheckReproducedVariant1ComponentsItem(TypedDict):
    component: str
    weightPips: int
    score: Union[int, None]

class HealthMarketQualityCheckReproducedVariant1(TypedDict):
    availability: Literal["AVAILABLE", "UNAVAILABLE"]
    score: Union[int, None]
    coveragePips: int
    components: list[HealthMarketQualityCheckReproducedVariant1ComponentsItem]

class HealthMarketQualityCheck(TypedDict):
    evidenceId: str
    period: Literal["CONTEXT", "BASELINE", "OBSERVATION"]
    algorithm: Literal["market-quality-score-v2"]
    arithmetic: Literal["REPRODUCED", "MISMATCH", "UNAVAILABLE"]
    sourceBindings: Literal["MATCHED", "MISMATCH", "INCOMPLETE"]
    rawMetrics: Literal["REPRODUCED", "MISMATCH", "UNAVAILABLE"]
    sourceEvidenceIds: list[str]
    issues: list[str]
    reproduced: Union[HealthMarketQualityCheckReproducedVariant1, None]
    verificationScope: Literal["DERIVED_SCORE_FIELDS_AND_CAPTURED_INPUTS"]
    signaturesAndQualification: Literal["NOT_REVERIFIED"]
    fullInputHash: Literal["MATCHED", "MISMATCH", "NOT_RECOMPUTED"]

class HealthClaim(TypedDict):
    claimId: str
    kind: Literal["RECORDED_FIELD", "CHECKED_COMPARISON", "CHECKED_MARKET_QUALITY"]
    label: str
    verification: Literal["RECORDED_SOURCE_ONLY", "EXACT_ARITHMETIC", "REPRODUCED_FROM_CAPTURED_INPUTS"]
    receipts: list[HealthFieldReceipt]
    comparison: NotRequired[HealthMetricComparison]
    marketQuality: NotRequired[HealthMarketQualityCheck]

class HealthCoverageGroup(TypedDict):
    sourceType: Literal["VAULT", "POLICY", "FINALIZED_SNAPSHOT", "MARKET_QUALITY_SCORE", "VENUE_OBSERVATION", "EXECUTION_ATTRIBUTION", "ANOMALY", "INCIDENT", "PROPOSAL"]
    period: Literal["CONTEXT", "BASELINE", "OBSERVATION"]
    candidateCount: int
    includedCount: int

class ValidatedHealthReportWindow(TypedDict):
    start: str
    end: str

class ValidatedHealthReportBaselineWindow(TypedDict):
    start: str
    end: str

class ValidatedHealthReportHypothesesItem(TypedDict):
    hypothesisId: str
    rank: int
    label: Literal["UNVERIFIED_HYPOTHESIS"]
    explanation: str
    supportingClaims: list[HealthClaim]
    contradictingClaims: list[HealthClaim]
    uncertainty: str
    warning: str

class ValidatedHealthReportNextChecksItem(TypedDict):
    kind: Literal["REVIEW_POLICY", "REVIEW_ACTIVITY", "REVIEW_INCIDENTS", "CHECK_DATA_HEALTH", "EXPLORE_RESEARCH_DRAFT"]
    label: str
    destination: Literal["POLICY", "ACTIVITY", "INCIDENTS", "DATA_HEALTH", "RESEARCH_SETUP"]
    execution: Literal["MANUAL_NAVIGATION_ONLY"]

class ValidatedHealthReportValidation(TypedDict):
    version: Literal["health-report-validator-v1"]
    checkedClaimCount: int
    recordedClaimCount: int
    availableClaimCount: int
    hypothesisSemanticsVerified: Literal[False]

class ValidatedHealthReport(TypedDict):
    schemaVersion: Literal["agent-health-report-v1"]
    organizationId: str
    runId: str
    captureHash: str
    sourceCutoff: str
    capturedAt: str
    window: ValidatedHealthReportWindow
    baselineWindow: ValidatedHealthReportBaselineWindow
    status: Literal["PARTIAL", "ABSTAINED"]
    marketHealth: Literal["NOT_ASSESSED"]
    title: str
    findings: list[HealthClaim]
    comparisons: list[HealthMetricComparison]
    marketQuality: list[HealthMarketQualityCheck]
    hypotheses: list[ValidatedHealthReportHypothesesItem]
    coverage: list[HealthCoverageGroup]
    gaps: list[str]
    nextChecks: list[ValidatedHealthReportNextChecksItem]
    validation: ValidatedHealthReportValidation

class SavedHealthResultProvenance(TypedDict):
    workflowVersion: str
    validatorVersion: Literal["health-report-validator-v1"]
    provider: str
    model: str
    modelVersion: str

class SavedHealthResultApplicability(TypedDict):
    status: Literal["SAME_SUBJECT_VERSION", "SUBJECT_CHANGED", "CURRENT_STATUS_UNAVAILABLE"]
    checkedAt: str
    savedSubjectVersion: str
    currentSubjectVersion: Union[str, None]
    scope: Literal["VAULT_RECORD_VERSION_ONLY"]

class SavedHealthResult(TypedDict):
    schemaVersion: Literal["agent-health-result-v1"]
    organizationId: str
    runId: str
    reportId: str
    resultVersion: str
    completedAt: str
    report: ValidatedHealthReport
    provenance: SavedHealthResultProvenance
    applicability: SavedHealthResultApplicability

class CapturedHealthEvidenceViewEvidenceCoverage(TypedDict):
    includedRecords: int
    excludedRecords: int
    truncated: bool
    gaps: list[str]

class CapturedHealthEvidenceViewEvidenceFieldsItem(TypedDict):
    field: str
    value: Union[Union[str, int, bool], None]

class CapturedHealthEvidenceViewEvidence(TypedDict):
    evidenceId: str
    source: HealthEvidenceSource
    temporalScope: Literal["HISTORICAL", "CURRENT_CONTEXT"]
    observedAt: Union[str, None]
    availableAt: Union[str, None]
    capturedAt: str
    sourceCutoff: str
    quoteAssetId: Union[str, None]
    finality: Literal["FINALIZED", "NOT_APPLICABLE", "UNKNOWN"]
    unit: Union[str, None]
    coverage: CapturedHealthEvidenceViewEvidenceCoverage
    sourceType: Literal["VAULT", "POLICY", "FINALIZED_SNAPSHOT", "MARKET_QUALITY_SCORE", "VENUE_OBSERVATION", "EXECUTION_ATTRIBUTION", "ANOMALY", "INCIDENT", "PROPOSAL"]
    period: Literal["CONTEXT", "BASELINE", "OBSERVATION"]
    fields: list[CapturedHealthEvidenceViewEvidenceFieldsItem]
    verification: Literal["RECORDED_SOURCE_ASSERTIONS"]

class CapturedHealthEvidenceView(TypedDict):
    schemaVersion: Literal["agent-health-evidence-view-v1"]
    organizationId: str
    runId: str
    captureHash: str
    evidence: CapturedHealthEvidenceViewEvidence

class ProjectHealthFindingMeasurementVariant1(TypedDict):
    asset: str
    decimals: Union[int, None]
    baselineAtomic: str
    observationAtomic: str
    changeAtomic: str

class ProjectHealthFinding(TypedDict):
    id: str
    summary: str
    evidenceSequences: list[str]
    measurement: Union[ProjectHealthFindingMeasurementVariant1, None]

class ProjectHealthReport(TypedDict):
    schemaVersion: Literal["agent-project-health-report-v1"]
    classification: Literal["PUBLIC_MARKET"]
    organizationId: str
    runId: str
    projectId: str
    captureHash: str
    sourceCutoff: str
    status: Literal["PARTIAL", "ABSTAINED"]
    marketHealth: Literal["NOT_ASSESSED"]
    findings: list[ProjectHealthFinding]
    gaps: list[str]
    nextChecks: list[Literal["REFRESH_PUBLIC_OBSERVATION", "VERIFY_TRANSFER_BEHAVIOR", "VERIFY_LIQUIDITY_CONTROL", "COLLECT_BASELINE_OBSERVATION"]]
    evidence: list[SavedProjectObservation]
    financialAuthority: Literal[False]

class SavedProjectHealthResultApplicability(TypedDict):
    scope: Literal["PROJECT_OBSERVATION_VERSION_ONLY"]
    status: Literal["SAME_SUBJECT_VERSION", "SUBJECT_CHANGED", "SUBJECT_UNAVAILABLE"]
    savedResourceVersion: str
    currentResourceVersion: Union[str, None]

class SavedProjectHealthResult(TypedDict):
    schemaVersion: Literal["saved-project-health-result-v1"]
    organizationId: str
    runId: str
    resultVersion: str
    completedAt: str
    report: ProjectHealthReport
    applicability: SavedProjectHealthResultApplicability

AgentHealthResult: TypeAlias = Union[SavedHealthResult, SavedProjectHealthResult]

class ProposalReviewSource(TypedDict):
    generation: Literal["V1", "V2"]
    recordType: Literal["PROPOSAL", "PROPOSAL_WORKSPACE"]
    recordId: str
    version: str
    artifactHash: Union[str, None]
    economicHash: str

class ProposalReviewDependency(TypedDict):
    kind: Literal["SIMULATION", "SIMULATION_STUDY", "STRATEGY_DEFINITION", "STRATEGY_ADMISSION", "POLICY_INTENT_DRAFT"]
    recordId: Union[str, None]
    resourceVersion: Union[str, None]
    artifactHash: Union[str, None]
    status: Literal["AVAILABLE", "UNAVAILABLE", "BINDING_MISMATCH"]
    recordedStatus: Union[str, None]

class ProposalReviewTokenFlow(TypedDict):
    token: str
    amountAtomic: str
    destination: str
    basis: Literal["PERSISTED_FLOW_NOT_EXECUTION_VERIFIED"]

class ProposalReviewFinding(TypedDict):
    id: str
    summary: str
    evidenceIds: list[str]

class ProposalReviewCheck(TypedDict):
    id: str
    status: Literal["RECORDED_PASS", "RECORDED_FAIL", "UNAVAILABLE", "NOT_APPLICABLE"]
    detail: str

class ProposalReviewReportMetricsItem(TypedDict):
    id: str
    valueAtomic: str
    quoteProfile: Union[str, None]
    unit: Literal["QUOTE_ATOMIC"]
    basis: Literal["PERSISTED_ASSERTION", "EXACT_DIFFERENCE_OF_ASSERTIONS"]

class ProposalReviewReportCostsItem(TypedDict):
    category: Literal["GAS", "INCENTIVE", "PLATFORM_FEE", "CAPITAL_LOSS", "VENUE_FEE", "SLIPPAGE"]
    status: Literal["DECLARED_ASSUMPTION", "UNAVAILABLE"]
    amountAtomic: Union[str, None]
    reason: str

class ProposalReviewReport(TypedDict):
    schemaVersion: Literal["agent-proposal-review-report-v1"]
    organizationId: str
    runId: str
    reviewScope: Literal["SAVED_PROPOSAL_EVIDENCE"]
    status: Literal["PARTIAL", "ABSTAINED"]
    reviewedAt: str
    sourceCutoff: str
    captureHash: str
    reviewedProposal: ProposalReviewSource
    findings: list[ProposalReviewFinding]
    checks: list[ProposalReviewCheck]
    metrics: list[ProposalReviewReportMetricsItem]
    costs: list[ProposalReviewReportCostsItem]
    tokenFlows: list[ProposalReviewTokenFlow]
    dependencies: list[ProposalReviewDependency]
    gaps: list[str]
    nextChecks: list[Literal["INSPECT_REFERENCED_EVIDENCE", "VERIFY_COMPLETE_COSTS", "REFRESH_PROPOSAL", "RECHECK_POLICY_AND_EXPIRY", "USE_EXISTING_HUMAN_APPROVAL_WORKFLOW"]]
    approvalAuthorityGranted: Literal[False]
    executionAuthorityGranted: Literal[False]

class SavedProposalReviewResultApplicability(TypedDict):
    scope: Literal["PROPOSAL_PACKET_AND_REFERENCED_GENERATIONS"]
    status: Literal["SAME_ECONOMIC_PACKET", "OPERATIONAL_STATUS_CHANGED", "ECONOMIC_PACKET_CHANGED", "SUBJECT_UNAVAILABLE"]
    checkedAt: str
    currentSourceVersion: Union[str, None]
    currentEconomicHash: Union[str, None]
    expired: Union[bool, None]
    dependenciesChanged: bool

class SavedProposalReviewResult(TypedDict):
    schemaVersion: Literal["saved-proposal-review-result-v1"]
    organizationId: str
    runId: str
    resultVersion: str
    completedAt: str
    report: ProposalReviewReport
    applicability: SavedProposalReviewResultApplicability

class CandidateReviewReportReviewedCandidate(TypedDict):
    packId: str
    resourceVersion: str
    contentHash: str

class CandidateReviewReportChecksItem(TypedDict):
    id: str
    status: Literal["RECORDED_PASS", "RECORDED_FAIL", "UNAVAILABLE"]
    detail: str

class CandidateReviewReportFindingsItem(TypedDict):
    id: str
    summary: str
    evidenceIds: list[str]

class CandidateReviewReportTrialReferencesItem(TypedDict):
    kind: Literal["RESEARCH_TRIAL"]
    runId: str
    protocolHash: str
    trialKey: Literal["baseline", "alternative-1", "alternative-2", "alternative-3"]
    inputHash: str
    artifactHash: Union[str, None]
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    recordedAt: Union[str, None]
    failureCode: Union[str, None]

class CandidateReviewReportCostsItem(TypedDict):
    category: Literal["GAS", "INCENTIVE", "PLATFORM_FEE", "CAPITAL_LOSS", "VENUE_FEE", "SLIPPAGE"]
    status: Literal["UNAVAILABLE"]
    amountAtomic: None
    reason: str

class CandidateReviewReport(TypedDict):
    schemaVersion: Literal["agent-candidate-review-report-v1"]
    organizationId: str
    runId: str
    reviewScope: Literal["RESEARCH_CANDIDATE_EVIDENCE"]
    status: Literal["PARTIAL"]
    captureHash: str
    sourceCutoff: str
    reviewedAt: str
    reviewedCandidate: CandidateReviewReportReviewedCandidate
    checks: list[CandidateReviewReportChecksItem]
    findings: list[CandidateReviewReportFindingsItem]
    trialReferences: list[CandidateReviewReportTrialReferencesItem]
    costs: list[CandidateReviewReportCostsItem]
    gaps: list[str]
    nextChecks: list[Literal["INSPECT_RESEARCH_TRIALS", "RESOLVE_MISSING_SCENARIOS", "VERIFY_PROJECT_AND_QUOTE_BINDING", "PREPARE_OPERATIONAL_PREREQUISITES", "USE_SEPARATE_HUMAN_APPROVAL"]]
    approvalAuthorityGranted: Literal[False]
    executionAuthorityGranted: Literal[False]
    publicationAuthorityGranted: Literal[False]

class SavedCandidateReviewResultReportReviewedCandidate(TypedDict):
    packId: str
    resourceVersion: str
    contentHash: str

class SavedCandidateReviewResultReportChecksItem(TypedDict):
    id: str
    status: Literal["RECORDED_PASS", "RECORDED_FAIL", "UNAVAILABLE"]
    detail: str

class SavedCandidateReviewResultReportFindingsItem(TypedDict):
    id: str
    summary: str
    evidenceIds: list[str]

class SavedCandidateReviewResultReportTrialReferencesItem(TypedDict):
    kind: Literal["RESEARCH_TRIAL"]
    runId: str
    protocolHash: str
    trialKey: Literal["baseline", "alternative-1", "alternative-2", "alternative-3"]
    inputHash: str
    artifactHash: Union[str, None]
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    recordedAt: Union[str, None]
    failureCode: Union[str, None]

class SavedCandidateReviewResultReportCostsItem(TypedDict):
    category: Literal["GAS", "INCENTIVE", "PLATFORM_FEE", "CAPITAL_LOSS", "VENUE_FEE", "SLIPPAGE"]
    status: Literal["UNAVAILABLE"]
    amountAtomic: None
    reason: str

class SavedCandidateReviewResultReport(TypedDict):
    schemaVersion: Literal["agent-candidate-review-report-v1"]
    organizationId: str
    runId: str
    reviewScope: Literal["RESEARCH_CANDIDATE_EVIDENCE"]
    status: Literal["PARTIAL"]
    captureHash: str
    sourceCutoff: str
    reviewedAt: str
    reviewedCandidate: SavedCandidateReviewResultReportReviewedCandidate
    checks: list[SavedCandidateReviewResultReportChecksItem]
    findings: list[SavedCandidateReviewResultReportFindingsItem]
    trialReferences: list[SavedCandidateReviewResultReportTrialReferencesItem]
    costs: list[SavedCandidateReviewResultReportCostsItem]
    gaps: list[str]
    nextChecks: list[Literal["INSPECT_RESEARCH_TRIALS", "RESOLVE_MISSING_SCENARIOS", "VERIFY_PROJECT_AND_QUOTE_BINDING", "PREPARE_OPERATIONAL_PREREQUISITES", "USE_SEPARATE_HUMAN_APPROVAL"]]
    approvalAuthorityGranted: Literal[False]
    executionAuthorityGranted: Literal[False]
    publicationAuthorityGranted: Literal[False]

class SavedCandidateReviewResultApplicability(TypedDict):
    scope: Literal["CANDIDATE_CONTENT_AND_REFERENCED_GENERATIONS"]
    status: Literal["SAME_CONTENT", "LIFECYCLE_CHANGED", "CONTENT_CHANGED", "SUBJECT_UNAVAILABLE"]
    checkedAt: str
    currentPackResourceVersion: Union[str, None]
    currentContentHash: Union[str, None]
    currentIssuerIntentResourceVersion: Union[str, None]
    currentProjectResourceVersion: Union[str, None]
    issuerIntentChanged: bool
    projectObservationChanged: bool

class SavedCandidateReviewResult(TypedDict):
    schemaVersion: Literal["saved-candidate-review-result-v1"]
    organizationId: str
    runId: str
    resultVersion: str
    completedAt: str
    report: SavedCandidateReviewResultReport
    applicability: SavedCandidateReviewResultApplicability

AgentRunResult: TypeAlias = Union[AgentHealthResult, SavedProposalReviewResult, SavedResearchResult, SavedCandidateReviewResult]

class AgentRunSummarySubjectWindow(TypedDict):
    start: str
    end: str

class AgentRunSummarySubjectBaselineWindow(TypedDict):
    start: str
    end: str

class AgentRunSummarySubject(TypedDict):
    generation: Literal["V1", "V2", "PROJECT", "DECISION_PACK"]
    recordType: Literal["VAULT", "PROPOSAL", "PROPOSAL_WORKSPACE", "ISSUER_INTENT", "SAVED_PUBLIC_PROJECT", "DECISION_PACK"]
    recordId: str
    vaultId: NotRequired[str]
    updatedAt: NotRequired[str]
    resourceVersion: NotRequired[str]
    observationSequence: NotRequired[str]
    baselineSequence: NotRequired[Union[str, None]]
    window: NotRequired[AgentRunSummarySubjectWindow]
    baselineWindow: NotRequired[AgentRunSummarySubjectBaselineWindow]

class AgentRunSummary(TypedDict):
    organizationId: str
    runId: str
    kind: Literal["HEALTH_INVESTIGATION", "PROPOSAL_REVIEW", "WHAT_IF_RESEARCH"]
    mode: NotRequired[Literal["PLAN"]]
    question: str
    state: Literal["QUEUED", "RUNNING", "WAITING_FOR_INPUT", "WAITING_FOR_CHILDREN", "COMPLETED", "PARTIAL", "ABSTAINED", "FAILED", "CANCELLED"]
    phase: Literal["ADMITTED", "CAPTURING_EVIDENCE", "CHECKING_SOURCES", "COMPARING_EVIDENCE", "PLANNING", "READING_EVIDENCE", "WAITING_FOR_INPUT", "WAITING_FOR_STUDIES", "VALIDATING_REPORT", "FINISHED"]
    sourceCutoff: str
    deadline: str
    createdAt: str
    updatedAt: str
    resourceVersion: str
    cancellationRequestedAt: Union[str, None]
    subject: AgentRunSummarySubject

class AgentClarificationOptionsItem(TypedDict):
    id: str
    label: str
    description: str

class AgentClarification(TypedDict):
    schemaVersion: Literal["agent-clarification-v1"]
    questionId: str
    prompt: str
    contextHash: str
    options: list[AgentClarificationOptionsItem]

class AgentRunLimits(TypedDict):
    maximumToolExecutions: int
    maximumOptionalToolCalls: int
    maximumModelAttempts: int
    maximumEvidenceRecords: int
    maximumEvidenceBytesPerRequest: int
    maximumTokens: int
    maximumCostMicrounits: str
    costCurrency: Literal["USD"]
    maximumResearchTrials: int
    maximumComputeUnits: int

class AgentRunDetailSteps(TypedDict):
    queued: int
    running: int
    completed: int
    failed: int
    uncertain: int

class AgentRunDetailControls(TypedDict):
    canCancel: bool
    canRespond: bool

class AgentRunDetail(TypedDict):
    run: AgentRunSummary
    pendingQuestion: Union[AgentClarification, None]
    steps: AgentRunDetailSteps
    activityHighWater: str
    limits: AgentRunLimits
    usage: None
    resultAvailable: bool
    controls: AgentRunDetailControls

class AgentRunList(TypedDict):
    runs: list[AgentRunSummary]
    nextCursor: Union[str, None]

class AgentActivityEvent(TypedDict):
    sequence: str
    kind: Literal["RUN_STATE", "STEP_STATE"]
    state: Literal["QUEUED", "RUNNING", "WAITING_FOR_INPUT", "WAITING_FOR_CHILDREN", "COMPLETED", "PARTIAL", "ABSTAINED", "FAILED", "CANCELLED"]
    phase: Literal["ADMITTED", "CAPTURING_EVIDENCE", "CHECKING_SOURCES", "COMPARING_EVIDENCE", "PLANNING", "READING_EVIDENCE", "WAITING_FOR_INPUT", "WAITING_FOR_STUDIES", "VALIDATING_REPORT", "FINISHED"]
    stepSequence: Union[int, None]
    stepKind: Union[Literal["SOURCE_CAPTURE", "DETERMINISTIC_CHECK", "TOOL_READ", "MODEL_CALL", "CLARIFICATION", "RESEARCH_DISPATCH", "RESEARCH_RESUME", "REPORT_VALIDATION"], None]
    stepState: Union[Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "UNCERTAIN"], None]
    occurredAt: str

class AgentActivityPage(TypedDict):
    organizationId: str
    runId: str
    events: list[AgentActivityEvent]
    nextAfter: str
    hasMore: bool
    highWater: str

class PublicProjectResolveRequest(TypedDict):
    identifier: str

class PublicProjectAnalysisTokenVariant1(TypedDict):
    address: str
    name: Union[str, None]
    symbol: Union[str, None]
    decimals: Union[int, None]

class PublicProjectAnalysisProject(TypedDict):
    virtualsProjectId: Union[str, None]
    url: Union[str, None]
    relationship: Literal["PUBLIC_IDENTIFIER_ONLY"]

class PublicProjectAnalysisLaunchStage(TypedDict):
    status: Literal["UNKNOWN", "POOL_OBSERVED"]
    explanation: str

class PublicProjectAnalysisObservationVariant1(TypedDict):
    blockNumber: str
    blockHash: str
    blockTimestamp: str
    observedAt: str
    readAt: str
    recordedAt: None
    providerId: str
    providerGeneration: str
    finality: Literal["FINALIZED"]
    finalityVerification: Literal["SINGLE_RPC_ASSERTION"]

class PublicProjectAnalysisPoolsItem(TypedDict):
    address: str
    factory: str
    token0: str
    token1: str
    reserve0Atomic: str
    reserve1Atomic: str
    reserve0Decimals: Union[int, None]
    reserve1Decimals: Union[int, None]
    verification: Literal["CANONICAL_FACTORY_AND_PAIR_AT_BLOCK"]
    quoteStatus: Literal["UNAVAILABLE_TRANSFER_BEHAVIOR"]

class PublicProjectAnalysis(TypedDict):
    schemaVersion: Literal["public-project-analysis-v1"]
    chainId: Literal[8453]
    identifier: str
    token: Union[PublicProjectAnalysisTokenVariant1, None]
    project: PublicProjectAnalysisProject
    launchStage: PublicProjectAnalysisLaunchStage
    observation: Union[PublicProjectAnalysisObservationVariant1, None]
    pools: list[PublicProjectAnalysisPoolsItem]
    gaps: list[str]
    financialAuthority: Literal[False]

class PublicLiquidityInvestigationRequest(TypedDict):
    identifier: str
    question: Literal["POOL_RESERVE_SCALE_V1"]
    quoteTradeSizeAtomic: Union[str, None]

class PublicLiquidityInvestigationFinding(TypedDict):
    state: Literal["AVAILABLE", "UNAVAILABLE"]
    poolAddress: Union[str, None]
    quoteReserveAtomic: Union[str, None]
    quoteDecimals: Union[int, None]
    sizeToReservePips: Union[str, None]
    reason: Literal["NO_QUOTE_SIZE", "NO_VERIFIED_POOL", "QUOTE_PRECISION_UNAVAILABLE", "ZERO_QUOTE_RESERVE", "SOURCE_INCONSISTENT", "VERIFIED_RESERVE_RATIO_ONLY"]

class PublicLiquidityInvestigation(TypedDict):
    schemaVersion: Literal["public-liquidity-investigation-v1"]
    question: Literal["POOL_RESERVE_SCALE_V1"]
    investigationId: str
    requestedQuoteSizeAtomic: Union[str, None]
    source: PublicProjectAnalysis
    finding: PublicLiquidityInvestigationFinding
    limitations: list[str]
    financialAuthority: Literal[False]

class SavedProjectObservation(TypedDict):
    sequence: str
    recordedAt: str
    resourceVersion: str
    analysis: PublicProjectAnalysis

class SavedProjectObservationMetadata(TypedDict):
    sequence: str
    recordedAt: str
    resourceVersion: str

class SavedPublicProject(TypedDict):
    organizationId: str
    projectId: str
    identifier: str
    tokenAddress: Union[str, None]
    createdAt: str
    updatedAt: str
    resourceVersion: str
    currentSequence: str
    latestObservation: SavedProjectObservation

class SavedProjectWriteReceipt(TypedDict):
    project: SavedPublicProject
    replayed: bool

class SavedProjectList(TypedDict):
    projects: list[SavedPublicProject]
    nextCursor: Union[str, None]

class SavedProjectObservationList(TypedDict):
    observations: list[SavedProjectObservationMetadata]
    nextCursor: Union[str, None]

class WorkspacePlanPrice(TypedDict):
    currency: Literal["USD"]
    amountMinor: str
    billingBasis: Literal["ONE_TIME", "MONTHLY", "ANNUAL"]

class WorkspacePlanLimits(TypedDict):
    projects: int
    teamSeats: int
    analyses: int
    analysisPeriod: Literal["ONE_TIME", "MONTHLY", "ANNUAL"]
    monitoringIntervalMinutes: Union[int, None]

class WorkspacePlan(TypedDict):
    id: str
    version: str
    name: str
    description: str
    price: WorkspacePlanPrice
    features: list[Literal["PUBLIC_ANALYSIS", "PRIVATE_TREASURY", "TEAM_COLLABORATION", "SCENARIO_RESEARCH", "PROPOSAL_REVIEW", "MONITORING", "DECISION_PACKS"]]
    limits: WorkspacePlanLimits
    overagePolicy: Literal["NO_AUTOMATIC_OVERAGE"]
    cancellationTerms: str

class WorkspacePlanCatalog(TypedDict):
    schemaVersion: Literal["workspace-plan-catalog-v1"]
    status: Literal["NOT_CONFIGURED", "PREVIEW"]
    catalogVersion: Union[str, None]
    validUntil: Union[str, None]
    plans: list[WorkspacePlan]
    purchaseAvailability: Literal["UNAVAILABLE"]
    financialAuthority: Literal[False]

class AcpOfferingRequirements(TypedDict):
    kind: Literal["PUBLIC_VIRTUALS_PROJECT"]
    chainId: Literal[8453]

class AcpOfferingDeliverable(TypedDict):
    kind: Literal["PUBLIC_PROJECT_ANALYSIS_V1"]

class AcpOfferingPrice(TypedDict):
    currency: Literal["USDC"]
    amountAtomic: str

class AcpOffering(TypedDict):
    id: str
    version: str
    name: str
    description: str
    requirements: AcpOfferingRequirements
    deliverable: AcpOfferingDeliverable
    price: AcpOfferingPrice
    slaMinutes: int
    fundTransfer: Literal[False]

class AcpOfferingPreview(TypedDict):
    schemaVersion: Literal["acp-offering-preview-v1"]
    status: Literal["NOT_CONFIGURED", "PREVIEW"]
    catalogVersion: Union[str, None]
    validUntil: Union[str, None]
    offering: Union[AcpOffering, None]
    purchaseAvailability: Literal["UNAVAILABLE"]
    financialAuthority: Literal[False]

class CreateDecisionPack(TypedDict):
    projectId: str
    observationSequence: str
    expectedProjectResourceVersion: str
    question: str
    assumptions: list[str]

class CreateTreasuryDecisionPack(TypedDict):
    projectionId: str
    projectionResourceVersion: str
    question: str
    assumptions: list[str]

class TreasuryScenarioDecisionPackProject(TypedDict):
    projectId: str
    observationSequence: str
    resourceVersion: str

class TreasuryScenarioDecisionPackHealthReportVariant1(TypedDict):
    question: str
    relation: Literal["SUPPORTING_EVIDENCE_ONLY"]
    runId: str
    resultVersion: str
    captureHash: str
    sourceCutoff: str
    status: Literal["PARTIAL", "ABSTAINED"]

class TreasuryScenarioDecisionPackAssumptions(TypedDict):
    version: str
    items: list[str]

class TreasuryScenarioDecisionPackReferencesTreasuryProjectionAssumptions(TypedDict):
    id: str
    resourceVersion: str

class TreasuryScenarioDecisionPackReferencesTreasuryProjectionReconciliation(TypedDict):
    id: str
    resourceVersion: str

class TreasuryScenarioDecisionPackReferencesTreasuryProjection(TypedDict):
    kind: Literal["DECLARED_TREASURY_SCENARIO"]
    projectionId: str
    resourceVersion: str
    modelHash: str
    sourceHash: str
    assumptions: TreasuryScenarioDecisionPackReferencesTreasuryProjectionAssumptions
    reconciliation: TreasuryScenarioDecisionPackReferencesTreasuryProjectionReconciliation
    sourceCutoff: str
    relation: Literal["HISTORICAL_SUPPORTING_EVIDENCE_ONLY"]
    provenance: Literal["DECLARED_SCENARIO"]
    spendability: Literal["NOT_ESTABLISHED"]

class TreasuryScenarioDecisionPackReferences(TypedDict):
    baselineStudy: None
    alternativeStudies: list[object]
    proposalReview: None
    treasuryProjection: TreasuryScenarioDecisionPackReferencesTreasuryProjection
    commercialOrder: None

class TreasuryScenarioDecisionPackDecisionVariant1(TypedDict):
    choice: Literal["DO_NOTHING", "REQUEST_MORE_EVIDENCE", "TAKE_TO_SEPARATE_APPROVAL"]
    rationale: str
    recordedBy: str
    recordedAt: str
    followUpAt: Union[str, None]

class TreasuryScenarioDecisionPackClosureVariant1(TypedDict):
    note: str
    recordedBy: str
    recordedAt: str

class TreasuryScenarioDecisionPack(TypedDict):
    schemaVersion: Literal["decision-pack-v3"]
    organizationId: str
    packId: str
    sequence: str
    resourceVersion: str
    createdAt: str
    recordedAt: str
    state: Literal["DRAFT", "READY_FOR_REVIEW", "DECISION_RECORDED", "FOLLOW_UP_DUE", "CLOSED", "SUPERSEDED"]
    scope: Literal["TREASURY_SCENARIO_REVIEW"]
    coverage: Literal["PARTIAL"]
    question: str
    project: TreasuryScenarioDecisionPackProject
    healthReport: Union[TreasuryScenarioDecisionPackHealthReportVariant1, None]
    assumptions: TreasuryScenarioDecisionPackAssumptions
    references: TreasuryScenarioDecisionPackReferences
    unsupportedReferences: list[object]
    decision: Union[TreasuryScenarioDecisionPackDecisionVariant1, None]
    closure: Union[TreasuryScenarioDecisionPackClosureVariant1, None]
    supersededBy: Union[str, None]
    financialAuthority: Literal[False]
    publicationAuthority: Literal[False]

class CreateResearchDecisionPack(TypedDict):
    projectId: str
    observationSequence: str
    expectedProjectResourceVersion: str
    question: str
    assumptions: list[str]
    researchRunId: str
    researchResultVersion: str
    expectedIssuerIntentResourceVersion: str
    selectedVariant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    association: Literal["USER_SELECTED_RESEARCH_CONTEXT"]

class PublicEvidenceDecisionPackProject(TypedDict):
    projectId: str
    observationSequence: str
    resourceVersion: str

class PublicEvidenceDecisionPackHealthReportVariant1(TypedDict):
    question: str
    relation: Literal["SUPPORTING_EVIDENCE_ONLY"]
    runId: str
    resultVersion: str
    captureHash: str
    sourceCutoff: str
    status: Literal["PARTIAL", "ABSTAINED"]

class PublicEvidenceDecisionPackAssumptions(TypedDict):
    version: str
    items: list[str]

class PublicEvidenceDecisionPackReferences(TypedDict):
    baselineStudy: None
    alternativeStudies: list[object]
    proposalReview: None
    treasuryProjection: None
    commercialOrder: None

class PublicEvidenceDecisionPackDecisionVariant1(TypedDict):
    choice: Literal["DO_NOTHING", "REQUEST_MORE_EVIDENCE", "TAKE_TO_SEPARATE_APPROVAL"]
    rationale: str
    recordedBy: str
    recordedAt: str
    followUpAt: Union[str, None]

class PublicEvidenceDecisionPackClosureVariant1(TypedDict):
    note: str
    recordedBy: str
    recordedAt: str

class PublicEvidenceDecisionPack(TypedDict):
    schemaVersion: Literal["decision-pack-v1"]
    organizationId: str
    packId: str
    sequence: str
    resourceVersion: str
    createdAt: str
    recordedAt: str
    state: Literal["DRAFT", "READY_FOR_REVIEW", "DECISION_RECORDED", "FOLLOW_UP_DUE", "CLOSED", "SUPERSEDED"]
    scope: Literal["PUBLIC_EVIDENCE_REVIEW"]
    coverage: Literal["PARTIAL"]
    question: str
    project: PublicEvidenceDecisionPackProject
    healthReport: Union[PublicEvidenceDecisionPackHealthReportVariant1, None]
    assumptions: PublicEvidenceDecisionPackAssumptions
    references: PublicEvidenceDecisionPackReferences
    unsupportedReferences: list[object]
    decision: Union[PublicEvidenceDecisionPackDecisionVariant1, None]
    closure: Union[PublicEvidenceDecisionPackClosureVariant1, None]
    supersededBy: Union[str, None]
    financialAuthority: Literal[False]
    publicationAuthority: Literal[False]

class ResearchCandidateDecisionPackProject(TypedDict):
    projectId: str
    observationSequence: str
    resourceVersion: str

class ResearchCandidateDecisionPackHealthReportVariant1(TypedDict):
    question: str
    relation: Literal["SUPPORTING_EVIDENCE_ONLY"]
    runId: str
    resultVersion: str
    captureHash: str
    sourceCutoff: str
    status: Literal["PARTIAL", "ABSTAINED"]

class ResearchCandidateDecisionPackAssumptions(TypedDict):
    version: str
    items: list[str]

class ResearchCandidateDecisionPackReferencesBaselineStudy(TypedDict):
    kind: Literal["RESEARCH_TRIAL"]
    runId: str
    protocolHash: str
    trialKey: Literal["baseline", "alternative-1", "alternative-2", "alternative-3"]
    inputHash: str
    artifactHash: Union[str, None]
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    recordedAt: Union[str, None]
    failureCode: Union[str, None]

class ResearchCandidateDecisionPackReferencesAlternativeStudiesItem(TypedDict):
    kind: Literal["RESEARCH_TRIAL"]
    runId: str
    protocolHash: str
    trialKey: Literal["baseline", "alternative-1", "alternative-2", "alternative-3"]
    inputHash: str
    artifactHash: Union[str, None]
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    recordedAt: Union[str, None]
    failureCode: Union[str, None]

class ResearchCandidateDecisionPackReferencesProposalReviewVariant1(TypedDict):
    kind: Literal["CANDIDATE_REVIEW"]
    runId: str
    resultVersion: str
    captureHash: str
    contentHash: str
    reviewedPackResourceVersion: str
    sourceCutoff: str
    status: Literal["PARTIAL"]
    relation: Literal["ANALYSIS_REVIEW_ONLY"]

class ResearchCandidateDecisionPackReferences(TypedDict):
    baselineStudy: ResearchCandidateDecisionPackReferencesBaselineStudy
    alternativeStudies: list[ResearchCandidateDecisionPackReferencesAlternativeStudiesItem]
    proposalReview: Union[ResearchCandidateDecisionPackReferencesProposalReviewVariant1, None]
    treasuryProjection: None
    commercialOrder: None

class ResearchCandidateDecisionPackDecisionVariant1(TypedDict):
    choice: Literal["DO_NOTHING", "REQUEST_MORE_EVIDENCE", "TAKE_TO_SEPARATE_APPROVAL"]
    rationale: str
    recordedBy: str
    recordedAt: str
    followUpAt: Union[str, None]

class ResearchCandidateDecisionPackClosureVariant1(TypedDict):
    note: str
    recordedBy: str
    recordedAt: str

class ResearchCandidateDecisionPackSourceAssociation(TypedDict):
    relation: Literal["USER_SELECTED_RESEARCH_CONTEXT"]
    assertedBy: str
    assertedAt: str
    ownershipVerified: Literal[False]
    quoteUnitsVerified: Literal[False]

class ResearchCandidateDecisionPackResearchIssuerIntent(TypedDict):
    id: str
    resourceVersion: str
    artifactHash: str

class ResearchCandidateDecisionPackResearchObjective(TypedDict):
    metric: Literal["ENDING_VALUE_P50", "MINIMUM_DEPTH_P5", "GAS_COST_P50", "DRAWDOWN_P95", "RESERVE_BREACH_PROBABILITY"]
    direction: Literal["MAXIMIZE", "MINIMIZE"]

class ResearchCandidateDecisionPackResearchQuote(TypedDict):
    symbol: str
    assetId: None
    decimals: None
    unit: Literal["ISSUER_INTENT_QUOTE_ATOMIC"]

class ResearchCandidateDecisionPackResearchTrialsItemReference(TypedDict):
    kind: Literal["RESEARCH_TRIAL"]
    runId: str
    protocolHash: str
    trialKey: Literal["baseline", "alternative-1", "alternative-2", "alternative-3"]
    inputHash: str
    artifactHash: Union[str, None]
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    recordedAt: Union[str, None]
    failureCode: Union[str, None]

class ResearchCandidateDecisionPackResearchTrialsItemSelectedVariant1(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    eligible: bool
    ineligibilityReasons: list[str]

class ResearchCandidateDecisionPackResearchTrialsItem(TypedDict):
    reference: ResearchCandidateDecisionPackResearchTrialsItemReference
    label: str
    comparisonStatus: Literal["PENDING", "FAILED", "CANCELLED", "INVALID", "INCOMPATIBLE", "BASELINE_UNAVAILABLE", "COMPARABLE"]
    reasons: list[str]
    warningCount: int
    selected: Union[ResearchCandidateDecisionPackResearchTrialsItemSelectedVariant1, None]

class ResearchCandidateDecisionPackResearch(TypedDict):
    runId: str
    resultVersion: str
    protocolHash: str
    sourceCutoff: str
    issuerIntent: ResearchCandidateDecisionPackResearchIssuerIntent
    question: str
    relation: Literal["SUPPORTING_EVIDENCE_ONLY"]
    objective: ResearchCandidateDecisionPackResearchObjective
    comparisonStatus: Literal["BASELINE_UNAVAILABLE", "COMPLETE", "PARTIAL"]
    quote: ResearchCandidateDecisionPackResearchQuote
    limitations: list[Literal["CURRENT_IS_ENGINE_GENERATED_NOT_ACTUAL_HOLDINGS", "COMPARISON_DOES_NOT_PROVE_EQUAL_CAPITAL_SUPERIORITY", "MARGINAL_PERCENTILE_DIFFERENCES_ARE_NOT_PAIRED_DIFFERENCE_PERCENTILES", "RESERVE_BREACH_IS_COMPOSITE_RESERVE_OR_ORACLE_BLOCKED_EVENT", "MODEL_OUTCOMES_ARE_NOT_FINANCIAL_GUARANTEES", "ARTIFACT_HASHES_DO_NOT_REPRODUCE_ENGINE_OUTPUT"]]
    trials: list[ResearchCandidateDecisionPackResearchTrialsItem]

class ResearchCandidateDecisionPackCandidateCapitalPlan(TypedDict):
    kind: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    requiredCapitalQuote: str
    deployableCapitalQuote: str
    stableReserveQuote: str
    emergencyReserveQuote: str
    rangeWidthPips: int
    expectedSlippagePips: int
    expectedFeeIncomeLowQuote: str
    expectedFeeIncomeHighQuote: str
    inventoryExposurePips: int
    maximumDailyTurnoverPips: int
    satisfiesIntent: bool
    reasons: list[str]

class ResearchCandidateDecisionPackCandidate(TypedDict):
    selectedVariant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    capitalPlan: ResearchCandidateDecisionPackCandidateCapitalPlan
    baselineEligible: bool
    status: Literal["BLOCKED_BASELINE_UNAVAILABLE", "BLOCKED_BASELINE_INELIGIBLE", "INCOMPLETE_ALTERNATIVES", "INELIGIBLE_IN_ALTERNATIVES", "ELIGIBLE_IN_CAPTURED_SCENARIOS"]
    rankingScope: Literal["WITHIN_SCENARIO_VARIANTS"]

class ResearchCandidateDecisionPack(TypedDict):
    schemaVersion: Literal["decision-pack-v2"]
    organizationId: str
    packId: str
    sequence: str
    resourceVersion: str
    createdAt: str
    recordedAt: str
    state: Literal["DRAFT", "READY_FOR_REVIEW", "DECISION_RECORDED", "FOLLOW_UP_DUE", "CLOSED", "SUPERSEDED"]
    scope: Literal["RESEARCH_CANDIDATE_REVIEW"]
    coverage: Literal["PARTIAL"]
    question: str
    project: ResearchCandidateDecisionPackProject
    healthReport: Union[ResearchCandidateDecisionPackHealthReportVariant1, None]
    assumptions: ResearchCandidateDecisionPackAssumptions
    references: ResearchCandidateDecisionPackReferences
    unsupportedReferences: Union[list[object], list[object]]
    decision: Union[ResearchCandidateDecisionPackDecisionVariant1, None]
    closure: Union[ResearchCandidateDecisionPackClosureVariant1, None]
    supersededBy: Union[str, None]
    financialAuthority: Literal[False]
    publicationAuthority: Literal[False]
    contentHash: str
    sourceAssociation: ResearchCandidateDecisionPackSourceAssociation
    research: ResearchCandidateDecisionPackResearch
    candidate: ResearchCandidateDecisionPackCandidate

class DecisionPackCommandVariant1(TypedDict):
    action: Literal["EDIT_DRAFT"]
    question: str
    assumptions: list[str]

class DecisionPackCommandVariant2(TypedDict):
    action: Literal["ATTACH_CANDIDATE_REVIEW"]
    runId: str
    resultVersion: str

class DecisionPackCommandVariant3(TypedDict):
    action: Literal["ATTACH_TREASURY_PROJECTION"]
    projectionId: str
    projectionResourceVersion: str

class DecisionPackCommandVariant4(TypedDict):
    action: Literal["ATTACH_HEALTH"]
    runId: str
    resultVersion: str

class DecisionPackCommandVariant5(TypedDict):
    action: Literal["READY_FOR_REVIEW"]

class DecisionPackCommandVariant6(TypedDict):
    action: Literal["RECORD_DECISION"]
    choice: Literal["DO_NOTHING", "REQUEST_MORE_EVIDENCE", "TAKE_TO_SEPARATE_APPROVAL"]
    rationale: str
    followUpAt: Union[str, None]

class DecisionPackCommandVariant7(TypedDict):
    action: Literal["MARK_FOLLOW_UP_DUE"]

class DecisionPackCommandVariant8(TypedDict):
    action: Literal["CLOSE"]
    note: str

class DecisionPackCommandVariant9(TypedDict):
    action: Literal["SUPERSEDE"]
    replacementPackId: str

DecisionPackCommand: TypeAlias = Union[DecisionPackCommandVariant1, DecisionPackCommandVariant2, DecisionPackCommandVariant3, DecisionPackCommandVariant4, DecisionPackCommandVariant5, DecisionPackCommandVariant6, DecisionPackCommandVariant7, DecisionPackCommandVariant8, DecisionPackCommandVariant9]

class DecisionPackVariant1Project(TypedDict):
    projectId: str
    observationSequence: str
    resourceVersion: str

class DecisionPackVariant1HealthReportVariant1(TypedDict):
    question: str
    relation: Literal["SUPPORTING_EVIDENCE_ONLY"]
    runId: str
    resultVersion: str
    captureHash: str
    sourceCutoff: str
    status: Literal["PARTIAL", "ABSTAINED"]

class DecisionPackVariant1Assumptions(TypedDict):
    version: str
    items: list[str]

class DecisionPackVariant1References(TypedDict):
    baselineStudy: None
    alternativeStudies: list[object]
    proposalReview: None
    treasuryProjection: None
    commercialOrder: None

class DecisionPackVariant1DecisionVariant1(TypedDict):
    choice: Literal["DO_NOTHING", "REQUEST_MORE_EVIDENCE", "TAKE_TO_SEPARATE_APPROVAL"]
    rationale: str
    recordedBy: str
    recordedAt: str
    followUpAt: Union[str, None]

class DecisionPackVariant1ClosureVariant1(TypedDict):
    note: str
    recordedBy: str
    recordedAt: str

class DecisionPackVariant1(TypedDict):
    schemaVersion: Literal["decision-pack-v1"]
    organizationId: str
    packId: str
    sequence: str
    resourceVersion: str
    createdAt: str
    recordedAt: str
    state: Literal["DRAFT", "READY_FOR_REVIEW", "DECISION_RECORDED", "FOLLOW_UP_DUE", "CLOSED", "SUPERSEDED"]
    scope: Literal["PUBLIC_EVIDENCE_REVIEW"]
    coverage: Literal["PARTIAL"]
    question: str
    project: DecisionPackVariant1Project
    healthReport: Union[DecisionPackVariant1HealthReportVariant1, None]
    assumptions: DecisionPackVariant1Assumptions
    references: DecisionPackVariant1References
    unsupportedReferences: list[object]
    decision: Union[DecisionPackVariant1DecisionVariant1, None]
    closure: Union[DecisionPackVariant1ClosureVariant1, None]
    supersededBy: Union[str, None]
    financialAuthority: Literal[False]
    publicationAuthority: Literal[False]

class DecisionPackVariant2Project(TypedDict):
    projectId: str
    observationSequence: str
    resourceVersion: str

class DecisionPackVariant2HealthReportVariant1(TypedDict):
    question: str
    relation: Literal["SUPPORTING_EVIDENCE_ONLY"]
    runId: str
    resultVersion: str
    captureHash: str
    sourceCutoff: str
    status: Literal["PARTIAL", "ABSTAINED"]

class DecisionPackVariant2Assumptions(TypedDict):
    version: str
    items: list[str]

class DecisionPackVariant2ReferencesBaselineStudy(TypedDict):
    kind: Literal["RESEARCH_TRIAL"]
    runId: str
    protocolHash: str
    trialKey: Literal["baseline", "alternative-1", "alternative-2", "alternative-3"]
    inputHash: str
    artifactHash: Union[str, None]
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    recordedAt: Union[str, None]
    failureCode: Union[str, None]

class DecisionPackVariant2ReferencesAlternativeStudiesItem(TypedDict):
    kind: Literal["RESEARCH_TRIAL"]
    runId: str
    protocolHash: str
    trialKey: Literal["baseline", "alternative-1", "alternative-2", "alternative-3"]
    inputHash: str
    artifactHash: Union[str, None]
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    recordedAt: Union[str, None]
    failureCode: Union[str, None]

class DecisionPackVariant2ReferencesProposalReviewVariant1(TypedDict):
    kind: Literal["CANDIDATE_REVIEW"]
    runId: str
    resultVersion: str
    captureHash: str
    contentHash: str
    reviewedPackResourceVersion: str
    sourceCutoff: str
    status: Literal["PARTIAL"]
    relation: Literal["ANALYSIS_REVIEW_ONLY"]

class DecisionPackVariant2References(TypedDict):
    baselineStudy: DecisionPackVariant2ReferencesBaselineStudy
    alternativeStudies: list[DecisionPackVariant2ReferencesAlternativeStudiesItem]
    proposalReview: Union[DecisionPackVariant2ReferencesProposalReviewVariant1, None]
    treasuryProjection: None
    commercialOrder: None

class DecisionPackVariant2DecisionVariant1(TypedDict):
    choice: Literal["DO_NOTHING", "REQUEST_MORE_EVIDENCE", "TAKE_TO_SEPARATE_APPROVAL"]
    rationale: str
    recordedBy: str
    recordedAt: str
    followUpAt: Union[str, None]

class DecisionPackVariant2ClosureVariant1(TypedDict):
    note: str
    recordedBy: str
    recordedAt: str

class DecisionPackVariant2SourceAssociation(TypedDict):
    relation: Literal["USER_SELECTED_RESEARCH_CONTEXT"]
    assertedBy: str
    assertedAt: str
    ownershipVerified: Literal[False]
    quoteUnitsVerified: Literal[False]

class DecisionPackVariant2ResearchIssuerIntent(TypedDict):
    id: str
    resourceVersion: str
    artifactHash: str

class DecisionPackVariant2ResearchObjective(TypedDict):
    metric: Literal["ENDING_VALUE_P50", "MINIMUM_DEPTH_P5", "GAS_COST_P50", "DRAWDOWN_P95", "RESERVE_BREACH_PROBABILITY"]
    direction: Literal["MAXIMIZE", "MINIMIZE"]

class DecisionPackVariant2ResearchQuote(TypedDict):
    symbol: str
    assetId: None
    decimals: None
    unit: Literal["ISSUER_INTENT_QUOTE_ATOMIC"]

class DecisionPackVariant2ResearchTrialsItemReference(TypedDict):
    kind: Literal["RESEARCH_TRIAL"]
    runId: str
    protocolHash: str
    trialKey: Literal["baseline", "alternative-1", "alternative-2", "alternative-3"]
    inputHash: str
    artifactHash: Union[str, None]
    state: Literal["QUEUED", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
    recordedAt: Union[str, None]
    failureCode: Union[str, None]

class DecisionPackVariant2ResearchTrialsItemSelectedVariant1(TypedDict):
    variant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    eligible: bool
    ineligibilityReasons: list[str]

class DecisionPackVariant2ResearchTrialsItem(TypedDict):
    reference: DecisionPackVariant2ResearchTrialsItemReference
    label: str
    comparisonStatus: Literal["PENDING", "FAILED", "CANCELLED", "INVALID", "INCOMPATIBLE", "BASELINE_UNAVAILABLE", "COMPARABLE"]
    reasons: list[str]
    warningCount: int
    selected: Union[DecisionPackVariant2ResearchTrialsItemSelectedVariant1, None]

class DecisionPackVariant2Research(TypedDict):
    runId: str
    resultVersion: str
    protocolHash: str
    sourceCutoff: str
    issuerIntent: DecisionPackVariant2ResearchIssuerIntent
    question: str
    relation: Literal["SUPPORTING_EVIDENCE_ONLY"]
    objective: DecisionPackVariant2ResearchObjective
    comparisonStatus: Literal["BASELINE_UNAVAILABLE", "COMPLETE", "PARTIAL"]
    quote: DecisionPackVariant2ResearchQuote
    limitations: list[Literal["CURRENT_IS_ENGINE_GENERATED_NOT_ACTUAL_HOLDINGS", "COMPARISON_DOES_NOT_PROVE_EQUAL_CAPITAL_SUPERIORITY", "MARGINAL_PERCENTILE_DIFFERENCES_ARE_NOT_PAIRED_DIFFERENCE_PERCENTILES", "RESERVE_BREACH_IS_COMPOSITE_RESERVE_OR_ORACLE_BLOCKED_EVENT", "MODEL_OUTCOMES_ARE_NOT_FINANCIAL_GUARANTEES", "ARTIFACT_HASHES_DO_NOT_REPRODUCE_ENGINE_OUTPUT"]]
    trials: list[DecisionPackVariant2ResearchTrialsItem]

class DecisionPackVariant2CandidateCapitalPlan(TypedDict):
    kind: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    requiredCapitalQuote: str
    deployableCapitalQuote: str
    stableReserveQuote: str
    emergencyReserveQuote: str
    rangeWidthPips: int
    expectedSlippagePips: int
    expectedFeeIncomeLowQuote: str
    expectedFeeIncomeHighQuote: str
    inventoryExposurePips: int
    maximumDailyTurnoverPips: int
    satisfiesIntent: bool
    reasons: list[str]

class DecisionPackVariant2Candidate(TypedDict):
    selectedVariant: Literal["CURRENT", "RECOMMENDED", "CONSERVATIVE", "CAPITAL_EFFICIENT", "EMERGENCY"]
    capitalPlan: DecisionPackVariant2CandidateCapitalPlan
    baselineEligible: bool
    status: Literal["BLOCKED_BASELINE_UNAVAILABLE", "BLOCKED_BASELINE_INELIGIBLE", "INCOMPLETE_ALTERNATIVES", "INELIGIBLE_IN_ALTERNATIVES", "ELIGIBLE_IN_CAPTURED_SCENARIOS"]
    rankingScope: Literal["WITHIN_SCENARIO_VARIANTS"]

class DecisionPackVariant2(TypedDict):
    schemaVersion: Literal["decision-pack-v2"]
    organizationId: str
    packId: str
    sequence: str
    resourceVersion: str
    createdAt: str
    recordedAt: str
    state: Literal["DRAFT", "READY_FOR_REVIEW", "DECISION_RECORDED", "FOLLOW_UP_DUE", "CLOSED", "SUPERSEDED"]
    scope: Literal["RESEARCH_CANDIDATE_REVIEW"]
    coverage: Literal["PARTIAL"]
    question: str
    project: DecisionPackVariant2Project
    healthReport: Union[DecisionPackVariant2HealthReportVariant1, None]
    assumptions: DecisionPackVariant2Assumptions
    references: DecisionPackVariant2References
    unsupportedReferences: Union[list[object], list[object]]
    decision: Union[DecisionPackVariant2DecisionVariant1, None]
    closure: Union[DecisionPackVariant2ClosureVariant1, None]
    supersededBy: Union[str, None]
    financialAuthority: Literal[False]
    publicationAuthority: Literal[False]
    contentHash: str
    sourceAssociation: DecisionPackVariant2SourceAssociation
    research: DecisionPackVariant2Research
    candidate: DecisionPackVariant2Candidate

class DecisionPackVariant3Project(TypedDict):
    projectId: str
    observationSequence: str
    resourceVersion: str

class DecisionPackVariant3HealthReportVariant1(TypedDict):
    question: str
    relation: Literal["SUPPORTING_EVIDENCE_ONLY"]
    runId: str
    resultVersion: str
    captureHash: str
    sourceCutoff: str
    status: Literal["PARTIAL", "ABSTAINED"]

class DecisionPackVariant3Assumptions(TypedDict):
    version: str
    items: list[str]

class DecisionPackVariant3ReferencesTreasuryProjectionAssumptions(TypedDict):
    id: str
    resourceVersion: str

class DecisionPackVariant3ReferencesTreasuryProjectionReconciliation(TypedDict):
    id: str
    resourceVersion: str

class DecisionPackVariant3ReferencesTreasuryProjection(TypedDict):
    kind: Literal["DECLARED_TREASURY_SCENARIO"]
    projectionId: str
    resourceVersion: str
    modelHash: str
    sourceHash: str
    assumptions: DecisionPackVariant3ReferencesTreasuryProjectionAssumptions
    reconciliation: DecisionPackVariant3ReferencesTreasuryProjectionReconciliation
    sourceCutoff: str
    relation: Literal["HISTORICAL_SUPPORTING_EVIDENCE_ONLY"]
    provenance: Literal["DECLARED_SCENARIO"]
    spendability: Literal["NOT_ESTABLISHED"]

class DecisionPackVariant3References(TypedDict):
    baselineStudy: None
    alternativeStudies: list[object]
    proposalReview: None
    treasuryProjection: DecisionPackVariant3ReferencesTreasuryProjection
    commercialOrder: None

class DecisionPackVariant3DecisionVariant1(TypedDict):
    choice: Literal["DO_NOTHING", "REQUEST_MORE_EVIDENCE", "TAKE_TO_SEPARATE_APPROVAL"]
    rationale: str
    recordedBy: str
    recordedAt: str
    followUpAt: Union[str, None]

class DecisionPackVariant3ClosureVariant1(TypedDict):
    note: str
    recordedBy: str
    recordedAt: str

class DecisionPackVariant3(TypedDict):
    schemaVersion: Literal["decision-pack-v3"]
    organizationId: str
    packId: str
    sequence: str
    resourceVersion: str
    createdAt: str
    recordedAt: str
    state: Literal["DRAFT", "READY_FOR_REVIEW", "DECISION_RECORDED", "FOLLOW_UP_DUE", "CLOSED", "SUPERSEDED"]
    scope: Literal["TREASURY_SCENARIO_REVIEW"]
    coverage: Literal["PARTIAL"]
    question: str
    project: DecisionPackVariant3Project
    healthReport: Union[DecisionPackVariant3HealthReportVariant1, None]
    assumptions: DecisionPackVariant3Assumptions
    references: DecisionPackVariant3References
    unsupportedReferences: list[object]
    decision: Union[DecisionPackVariant3DecisionVariant1, None]
    closure: Union[DecisionPackVariant3ClosureVariant1, None]
    supersededBy: Union[str, None]
    financialAuthority: Literal[False]
    publicationAuthority: Literal[False]

DecisionPack: TypeAlias = Union[DecisionPackVariant1, DecisionPackVariant2, DecisionPackVariant3]

class DecisionPackWriteReceipt(TypedDict):
    pack: DecisionPack
    replayed: bool

class DecisionPackList(TypedDict):
    packs: list[DecisionPack]
    nextCursor: Union[str, None]

class DecisionPackHistoryVersionsItem(TypedDict):
    sequence: str
    resourceVersion: str
    state: Literal["DRAFT", "READY_FOR_REVIEW", "DECISION_RECORDED", "FOLLOW_UP_DUE", "CLOSED", "SUPERSEDED"]
    recordedAt: str

class DecisionPackHistory(TypedDict):
    versions: list[DecisionPackHistoryVersionsItem]
    nextCursor: Union[str, None]

class SignedTreasuryEvidencePayloadRelationship(TypedDict):
    id: str
    resourceVersion: str
    evidenceHash: str

class SignedTreasuryEvidencePayloadProvider(TypedDict):
    id: str
    resourceVersion: str
    attestationHash: str

class SignedTreasuryEvidencePayloadObservation(TypedDict):
    chainId: int
    genesisHash: str
    token: str
    decimals: int
    custodyAccount: str
    amountAtomic: str
    blockNumber: str
    blockHash: str
    blockTimestamp: str
    finality: Literal["FINALIZED"]

class SignedTreasuryEvidencePayload(TypedDict):
    schemaVersion: Literal["treasury-custody-evidence-v1"]
    organizationId: str
    projectId: str
    evidenceId: str
    relationship: SignedTreasuryEvidencePayloadRelationship
    provider: SignedTreasuryEvidencePayloadProvider
    observation: SignedTreasuryEvidencePayloadObservation
    observedAt: str
    sourceCutoff: str
    expiresAt: str

class SignedTreasuryEvidence(TypedDict):
    payload: SignedTreasuryEvidencePayload
    payloadHash: str
    signature: str

class PersistedTreasuryEvidenceVerificationEvidencePayloadRelationship(TypedDict):
    id: str
    resourceVersion: str
    evidenceHash: str

class PersistedTreasuryEvidenceVerificationEvidencePayloadProvider(TypedDict):
    id: str
    resourceVersion: str
    attestationHash: str

class PersistedTreasuryEvidenceVerificationEvidencePayloadObservation(TypedDict):
    chainId: int
    genesisHash: str
    token: str
    decimals: int
    custodyAccount: str
    amountAtomic: str
    blockNumber: str
    blockHash: str
    blockTimestamp: str
    finality: Literal["FINALIZED"]

class PersistedTreasuryEvidenceVerificationEvidencePayload(TypedDict):
    schemaVersion: Literal["treasury-custody-evidence-v1"]
    organizationId: str
    projectId: str
    evidenceId: str
    relationship: PersistedTreasuryEvidenceVerificationEvidencePayloadRelationship
    provider: PersistedTreasuryEvidenceVerificationEvidencePayloadProvider
    observation: PersistedTreasuryEvidenceVerificationEvidencePayloadObservation
    observedAt: str
    sourceCutoff: str
    expiresAt: str

class PersistedTreasuryEvidenceVerificationEvidence(TypedDict):
    payload: PersistedTreasuryEvidenceVerificationEvidencePayload
    payloadHash: str
    signature: str

class PersistedTreasuryEvidenceVerificationObservation(TypedDict):
    chainId: int
    genesisHash: str
    token: str
    decimals: int
    custodyAccount: str
    amountAtomic: str
    blockNumber: str
    blockHash: str
    blockTimestamp: str
    finality: Literal["FINALIZED"]

class PersistedTreasuryEvidenceVerificationAuthorityRelationship(TypedDict):
    id: str
    resourceVersion: str
    evidenceHash: str

class PersistedTreasuryEvidenceVerificationAuthorityProvider(TypedDict):
    id: str
    resourceVersion: str
    attestationHash: str

class PersistedTreasuryEvidenceVerificationAuthority(TypedDict):
    relationship: PersistedTreasuryEvidenceVerificationAuthorityRelationship
    provider: PersistedTreasuryEvidenceVerificationAuthorityProvider

class PersistedTreasuryEvidenceVerificationQuorum(TypedDict):
    kind: Literal["CONFIGURED_OPERATOR_MAJORITY"]
    members: Union[Literal[3], Literal[5], Literal[7]]
    required: int

class PersistedTreasuryEvidenceVerification(TypedDict):
    schemaVersion: Literal["verified-treasury-custody-evidence-v1"]
    evidence: PersistedTreasuryEvidenceVerificationEvidence
    observation: PersistedTreasuryEvidenceVerificationObservation
    checkedAt: str
    authority: PersistedTreasuryEvidenceVerificationAuthority
    quorum: PersistedTreasuryEvidenceVerificationQuorum
    replayProtection: Literal["REQUIRES_PERSISTED_EVIDENCE_ID_UNIQUENESS"]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class PersistedTreasuryEvidence(TypedDict):
    schemaVersion: Literal["persisted-treasury-custody-evidence-v1"]
    organizationId: str
    evidenceId: str
    resourceVersion: str
    recordedAt: str
    recordedBy: str
    verification: PersistedTreasuryEvidenceVerification
    replayProtection: Literal["TENANT_EVIDENCE_ID_EXACT_CONTENT"]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryEvidenceWriteRecordVerificationEvidencePayloadRelationship(TypedDict):
    id: str
    resourceVersion: str
    evidenceHash: str

class TreasuryEvidenceWriteRecordVerificationEvidencePayloadProvider(TypedDict):
    id: str
    resourceVersion: str
    attestationHash: str

class TreasuryEvidenceWriteRecordVerificationEvidencePayloadObservation(TypedDict):
    chainId: int
    genesisHash: str
    token: str
    decimals: int
    custodyAccount: str
    amountAtomic: str
    blockNumber: str
    blockHash: str
    blockTimestamp: str
    finality: Literal["FINALIZED"]

class TreasuryEvidenceWriteRecordVerificationEvidencePayload(TypedDict):
    schemaVersion: Literal["treasury-custody-evidence-v1"]
    organizationId: str
    projectId: str
    evidenceId: str
    relationship: TreasuryEvidenceWriteRecordVerificationEvidencePayloadRelationship
    provider: TreasuryEvidenceWriteRecordVerificationEvidencePayloadProvider
    observation: TreasuryEvidenceWriteRecordVerificationEvidencePayloadObservation
    observedAt: str
    sourceCutoff: str
    expiresAt: str

class TreasuryEvidenceWriteRecordVerificationEvidence(TypedDict):
    payload: TreasuryEvidenceWriteRecordVerificationEvidencePayload
    payloadHash: str
    signature: str

class TreasuryEvidenceWriteRecordVerificationObservation(TypedDict):
    chainId: int
    genesisHash: str
    token: str
    decimals: int
    custodyAccount: str
    amountAtomic: str
    blockNumber: str
    blockHash: str
    blockTimestamp: str
    finality: Literal["FINALIZED"]

class TreasuryEvidenceWriteRecordVerificationAuthorityRelationship(TypedDict):
    id: str
    resourceVersion: str
    evidenceHash: str

class TreasuryEvidenceWriteRecordVerificationAuthorityProvider(TypedDict):
    id: str
    resourceVersion: str
    attestationHash: str

class TreasuryEvidenceWriteRecordVerificationAuthority(TypedDict):
    relationship: TreasuryEvidenceWriteRecordVerificationAuthorityRelationship
    provider: TreasuryEvidenceWriteRecordVerificationAuthorityProvider

class TreasuryEvidenceWriteRecordVerificationQuorum(TypedDict):
    kind: Literal["CONFIGURED_OPERATOR_MAJORITY"]
    members: Union[Literal[3], Literal[5], Literal[7]]
    required: int

class TreasuryEvidenceWriteRecordVerification(TypedDict):
    schemaVersion: Literal["verified-treasury-custody-evidence-v1"]
    evidence: TreasuryEvidenceWriteRecordVerificationEvidence
    observation: TreasuryEvidenceWriteRecordVerificationObservation
    checkedAt: str
    authority: TreasuryEvidenceWriteRecordVerificationAuthority
    quorum: TreasuryEvidenceWriteRecordVerificationQuorum
    replayProtection: Literal["REQUIRES_PERSISTED_EVIDENCE_ID_UNIQUENESS"]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryEvidenceWriteRecord(TypedDict):
    schemaVersion: Literal["persisted-treasury-custody-evidence-v1"]
    organizationId: str
    evidenceId: str
    resourceVersion: str
    recordedAt: str
    recordedBy: str
    verification: TreasuryEvidenceWriteRecordVerification
    replayProtection: Literal["TENANT_EVIDENCE_ID_EXACT_CONTENT"]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryEvidenceWrite(TypedDict):
    record: TreasuryEvidenceWriteRecord
    replayed: bool

class TreasuryEvidenceListRecordsItemVerificationEvidencePayloadRelationship(TypedDict):
    id: str
    resourceVersion: str
    evidenceHash: str

class TreasuryEvidenceListRecordsItemVerificationEvidencePayloadProvider(TypedDict):
    id: str
    resourceVersion: str
    attestationHash: str

class TreasuryEvidenceListRecordsItemVerificationEvidencePayloadObservation(TypedDict):
    chainId: int
    genesisHash: str
    token: str
    decimals: int
    custodyAccount: str
    amountAtomic: str
    blockNumber: str
    blockHash: str
    blockTimestamp: str
    finality: Literal["FINALIZED"]

class TreasuryEvidenceListRecordsItemVerificationEvidencePayload(TypedDict):
    schemaVersion: Literal["treasury-custody-evidence-v1"]
    organizationId: str
    projectId: str
    evidenceId: str
    relationship: TreasuryEvidenceListRecordsItemVerificationEvidencePayloadRelationship
    provider: TreasuryEvidenceListRecordsItemVerificationEvidencePayloadProvider
    observation: TreasuryEvidenceListRecordsItemVerificationEvidencePayloadObservation
    observedAt: str
    sourceCutoff: str
    expiresAt: str

class TreasuryEvidenceListRecordsItemVerificationEvidence(TypedDict):
    payload: TreasuryEvidenceListRecordsItemVerificationEvidencePayload
    payloadHash: str
    signature: str

class TreasuryEvidenceListRecordsItemVerificationObservation(TypedDict):
    chainId: int
    genesisHash: str
    token: str
    decimals: int
    custodyAccount: str
    amountAtomic: str
    blockNumber: str
    blockHash: str
    blockTimestamp: str
    finality: Literal["FINALIZED"]

class TreasuryEvidenceListRecordsItemVerificationAuthorityRelationship(TypedDict):
    id: str
    resourceVersion: str
    evidenceHash: str

class TreasuryEvidenceListRecordsItemVerificationAuthorityProvider(TypedDict):
    id: str
    resourceVersion: str
    attestationHash: str

class TreasuryEvidenceListRecordsItemVerificationAuthority(TypedDict):
    relationship: TreasuryEvidenceListRecordsItemVerificationAuthorityRelationship
    provider: TreasuryEvidenceListRecordsItemVerificationAuthorityProvider

class TreasuryEvidenceListRecordsItemVerificationQuorum(TypedDict):
    kind: Literal["CONFIGURED_OPERATOR_MAJORITY"]
    members: Union[Literal[3], Literal[5], Literal[7]]
    required: int

class TreasuryEvidenceListRecordsItemVerification(TypedDict):
    schemaVersion: Literal["verified-treasury-custody-evidence-v1"]
    evidence: TreasuryEvidenceListRecordsItemVerificationEvidence
    observation: TreasuryEvidenceListRecordsItemVerificationObservation
    checkedAt: str
    authority: TreasuryEvidenceListRecordsItemVerificationAuthority
    quorum: TreasuryEvidenceListRecordsItemVerificationQuorum
    replayProtection: Literal["REQUIRES_PERSISTED_EVIDENCE_ID_UNIQUENESS"]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryEvidenceListRecordsItem(TypedDict):
    schemaVersion: Literal["persisted-treasury-custody-evidence-v1"]
    organizationId: str
    evidenceId: str
    resourceVersion: str
    recordedAt: str
    recordedBy: str
    verification: TreasuryEvidenceListRecordsItemVerification
    replayProtection: Literal["TENANT_EVIDENCE_ID_EXACT_CONTENT"]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryEvidenceList(TypedDict):
    records: list[TreasuryEvidenceListRecordsItem]
    nextCursor: Union[str, None]

class ProjectControlIssueIdentityPayloadPublisher(TypedDict):
    id: str
    resourceVersion: str

class ProjectControlIssueIdentityPayload(TypedDict):
    organizationId: str
    projectId: str
    projectResourceVersion: str
    chainId: int
    genesisHash: str
    token: str
    schemaVersion: Literal["project-identity-attestation-v1"]
    publisher: ProjectControlIssueIdentityPayloadPublisher
    controller: str
    issuedAt: int
    expiresAt: int

class ProjectControlIssueIdentity(TypedDict):
    payload: ProjectControlIssueIdentityPayload
    payloadHash: str
    signature: str

class ProjectControlIssue(TypedDict):
    identity: ProjectControlIssueIdentity
    custodyAccount: str

class ProjectControlProofChallenge(TypedDict):
    organizationId: str
    projectId: str
    projectResourceVersion: str
    chainId: int
    genesisHash: str
    token: str
    schemaVersion: Literal["project-control-challenge-v1"]
    actorId: str
    controller: str
    custodyAccount: str
    attestationHash: str
    nonce: str
    audience: str
    deployment: str
    purpose: Literal["PROJECT_TREASURY_READ_ACCESS_ONLY"]
    issuedAt: int
    expiresAt: int

class ProjectControlProofIdentityPayloadPublisher(TypedDict):
    id: str
    resourceVersion: str

class ProjectControlProofIdentityPayload(TypedDict):
    organizationId: str
    projectId: str
    projectResourceVersion: str
    chainId: int
    genesisHash: str
    token: str
    schemaVersion: Literal["project-identity-attestation-v1"]
    publisher: ProjectControlProofIdentityPayloadPublisher
    controller: str
    issuedAt: int
    expiresAt: int

class ProjectControlProofIdentity(TypedDict):
    payload: ProjectControlProofIdentityPayload
    payloadHash: str
    signature: str

class ProjectControlProof(TypedDict):
    challenge: ProjectControlProofChallenge
    identity: ProjectControlProofIdentity
    controllerSignature: str
    custodySignature: str

class PersistedProjectControlChallengeChallenge(TypedDict):
    organizationId: str
    projectId: str
    projectResourceVersion: str
    chainId: int
    genesisHash: str
    token: str
    schemaVersion: Literal["project-control-challenge-v1"]
    actorId: str
    controller: str
    custodyAccount: str
    attestationHash: str
    nonce: str
    audience: str
    deployment: str
    purpose: Literal["PROJECT_TREASURY_READ_ACCESS_ONLY"]
    issuedAt: int
    expiresAt: int

class PersistedProjectControlChallengeIdentityPayloadPublisher(TypedDict):
    id: str
    resourceVersion: str

class PersistedProjectControlChallengeIdentityPayload(TypedDict):
    organizationId: str
    projectId: str
    projectResourceVersion: str
    chainId: int
    genesisHash: str
    token: str
    schemaVersion: Literal["project-identity-attestation-v1"]
    publisher: PersistedProjectControlChallengeIdentityPayloadPublisher
    controller: str
    issuedAt: int
    expiresAt: int

class PersistedProjectControlChallengeIdentity(TypedDict):
    payload: PersistedProjectControlChallengeIdentityPayload
    payloadHash: str
    signature: str

class PersistedProjectControlChallengeAnchor(TypedDict):
    chainId: int
    genesisHash: str
    blockNumber: str
    blockHash: str
    finality: Literal["FINALIZED"]

class PersistedProjectControlChallenge(TypedDict):
    schemaVersion: Literal["persisted-project-control-challenge-v1"]
    challenge: PersistedProjectControlChallengeChallenge
    identity: PersistedProjectControlChallengeIdentity
    anchor: PersistedProjectControlChallengeAnchor
    resourceVersion: str
    recordedAt: str

class ProjectControlChallengeWriteRecordChallenge(TypedDict):
    organizationId: str
    projectId: str
    projectResourceVersion: str
    chainId: int
    genesisHash: str
    token: str
    schemaVersion: Literal["project-control-challenge-v1"]
    actorId: str
    controller: str
    custodyAccount: str
    attestationHash: str
    nonce: str
    audience: str
    deployment: str
    purpose: Literal["PROJECT_TREASURY_READ_ACCESS_ONLY"]
    issuedAt: int
    expiresAt: int

class ProjectControlChallengeWriteRecordIdentityPayloadPublisher(TypedDict):
    id: str
    resourceVersion: str

class ProjectControlChallengeWriteRecordIdentityPayload(TypedDict):
    organizationId: str
    projectId: str
    projectResourceVersion: str
    chainId: int
    genesisHash: str
    token: str
    schemaVersion: Literal["project-identity-attestation-v1"]
    publisher: ProjectControlChallengeWriteRecordIdentityPayloadPublisher
    controller: str
    issuedAt: int
    expiresAt: int

class ProjectControlChallengeWriteRecordIdentity(TypedDict):
    payload: ProjectControlChallengeWriteRecordIdentityPayload
    payloadHash: str
    signature: str

class ProjectControlChallengeWriteRecordAnchor(TypedDict):
    chainId: int
    genesisHash: str
    blockNumber: str
    blockHash: str
    finality: Literal["FINALIZED"]

class ProjectControlChallengeWriteRecord(TypedDict):
    schemaVersion: Literal["persisted-project-control-challenge-v1"]
    challenge: ProjectControlChallengeWriteRecordChallenge
    identity: ProjectControlChallengeWriteRecordIdentity
    anchor: ProjectControlChallengeWriteRecordAnchor
    resourceVersion: str
    recordedAt: str

class ProjectControlChallengeWrite(TypedDict):
    record: ProjectControlChallengeWriteRecord
    replayed: bool

class ProjectControlAcceptanceRelationship(TypedDict):
    organizationId: str
    id: str
    resourceVersion: str
    evidenceHash: str
    projectId: str
    chainId: int
    genesisHash: str
    custodyAccount: str
    status: Literal["ACTIVE"]
    validFrom: str
    validUntil: str
    verification: Literal["PROJECT_AND_CUSTODY_CONTROL"]

class ProjectControlAcceptance(TypedDict):
    relationship: ProjectControlAcceptanceRelationship
    proofHash: str
    recordedAt: str
    replayed: bool

class TreasuryReconciliationPreviewRequestMappingsItemLedger(TypedDict):
    recordId: str
    resourceVersion: str
    artifactHash: str

class TreasuryReconciliationPreviewRequestMappingsItemCustody(TypedDict):
    evidenceId: str
    resourceVersion: str

class TreasuryReconciliationPreviewRequestMappingsItem(TypedDict):
    ledger: TreasuryReconciliationPreviewRequestMappingsItemLedger
    custody: TreasuryReconciliationPreviewRequestMappingsItemCustody

class TreasuryReconciliationPreviewRequest(TypedDict):
    mappings: list[TreasuryReconciliationPreviewRequestMappingsItem]

class TreasuryLedgerReconciliationMappingsItemLedger(TypedDict):
    recordId: str
    resourceVersion: str
    artifactHash: str

class TreasuryLedgerReconciliationMappingsItemCustody(TypedDict):
    evidenceId: str
    resourceVersion: str

class TreasuryLedgerReconciliationMappingsItemDeclaredSource(TypedDict):
    kind: Literal["SAFE", "VAULT", "EXTERNAL_MANAGER"]
    id: str

class TreasuryLedgerReconciliationMappingsItemUnit(TypedDict):
    chainId: int
    genesisHash: str
    asset: str
    decimals: int

class TreasuryLedgerReconciliationMappingsItemRelationship(TypedDict):
    id: str
    resourceVersion: str
    evidenceHash: str

class TreasuryLedgerReconciliationMappingsItemBlock(TypedDict):
    number: str
    hash: str
    timestamp: str

class TreasuryLedgerReconciliationMappingsItem(TypedDict):
    ledger: TreasuryLedgerReconciliationMappingsItemLedger
    custody: TreasuryLedgerReconciliationMappingsItemCustody
    capitalContainerId: str
    declaredCustodyLocationId: str
    declaredSource: TreasuryLedgerReconciliationMappingsItemDeclaredSource
    unit: TreasuryLedgerReconciliationMappingsItemUnit
    custodyAccount: str
    relationship: TreasuryLedgerReconciliationMappingsItemRelationship
    projectId: str
    block: TreasuryLedgerReconciliationMappingsItemBlock
    ledgerAmountAtomic: str
    observedCustodyAmountAtomic: str
    unallocatedCustodySurplusAtomic: str
    ledgerState: Literal["AVAILABLE", "DEPLOYED", "LOCKED", "AT_RISK", "FEE_GENERATING"]
    committedQuoteValuation: str
    obligationIds: list[str]
    disposition: Literal["PROPOSED_MAPPING_REQUIRES_ADMISSION"]

class TreasuryLedgerReconciliationSourceBindingsLedgerItem(TypedDict):
    recordId: str
    resourceVersion: str
    artifactHash: str

class TreasuryLedgerReconciliationSourceBindingsCustodyItem(TypedDict):
    evidenceId: str
    resourceVersion: str

class TreasuryLedgerReconciliationSourceBindings(TypedDict):
    ledger: list[TreasuryLedgerReconciliationSourceBindingsLedgerItem]
    custody: list[TreasuryLedgerReconciliationSourceBindingsCustodyItem]

class TreasuryLedgerReconciliationLedgerConservation(TypedDict):
    scope: Literal["SUPPLIED_IMMUTABLE_ENTRIES_ONLY"]
    ledgerVersion: Literal["treasury-ledger-v1", "treasury-ledger-v2"]
    conserved: Literal[True]
    commitment: str

class TreasuryLedgerReconciliation(TypedDict):
    schemaVersion: Literal["treasury-ledger-custody-reconciliation-candidate-v1"]
    organizationId: str
    sourceCutoff: str
    status: Literal["REVIEW_CANDIDATE"]
    mappings: list[TreasuryLedgerReconciliationMappingsItem]
    sourceBindings: TreasuryLedgerReconciliationSourceBindings
    sourceHash: str
    candidateHash: str
    ledgerConservation: TreasuryLedgerReconciliationLedgerConservation
    omittedLedgerEntryIds: list[str]
    omittedCustodyEvidenceIds: list[str]
    limitations: list[object]
    spendability: Literal["NOT_ESTABLISHED"]
    expenseCoverage: Literal["UNKNOWN"]
    financialAuthority: Literal[False]

class SavedTreasuryReconciliationCandidateMappingsItemLedger(TypedDict):
    recordId: str
    resourceVersion: str
    artifactHash: str

class SavedTreasuryReconciliationCandidateMappingsItemCustody(TypedDict):
    evidenceId: str
    resourceVersion: str

class SavedTreasuryReconciliationCandidateMappingsItemDeclaredSource(TypedDict):
    kind: Literal["SAFE", "VAULT", "EXTERNAL_MANAGER"]
    id: str

class SavedTreasuryReconciliationCandidateMappingsItemUnit(TypedDict):
    chainId: int
    genesisHash: str
    asset: str
    decimals: int

class SavedTreasuryReconciliationCandidateMappingsItemRelationship(TypedDict):
    id: str
    resourceVersion: str
    evidenceHash: str

class SavedTreasuryReconciliationCandidateMappingsItemBlock(TypedDict):
    number: str
    hash: str
    timestamp: str

class SavedTreasuryReconciliationCandidateMappingsItem(TypedDict):
    ledger: SavedTreasuryReconciliationCandidateMappingsItemLedger
    custody: SavedTreasuryReconciliationCandidateMappingsItemCustody
    capitalContainerId: str
    declaredCustodyLocationId: str
    declaredSource: SavedTreasuryReconciliationCandidateMappingsItemDeclaredSource
    unit: SavedTreasuryReconciliationCandidateMappingsItemUnit
    custodyAccount: str
    relationship: SavedTreasuryReconciliationCandidateMappingsItemRelationship
    projectId: str
    block: SavedTreasuryReconciliationCandidateMappingsItemBlock
    ledgerAmountAtomic: str
    observedCustodyAmountAtomic: str
    unallocatedCustodySurplusAtomic: str
    ledgerState: Literal["AVAILABLE", "DEPLOYED", "LOCKED", "AT_RISK", "FEE_GENERATING"]
    committedQuoteValuation: str
    obligationIds: list[str]
    disposition: Literal["PROPOSED_MAPPING_REQUIRES_ADMISSION"]

class SavedTreasuryReconciliationCandidateSourceBindingsLedgerItem(TypedDict):
    recordId: str
    resourceVersion: str
    artifactHash: str

class SavedTreasuryReconciliationCandidateSourceBindingsCustodyItem(TypedDict):
    evidenceId: str
    resourceVersion: str

class SavedTreasuryReconciliationCandidateSourceBindings(TypedDict):
    ledger: list[SavedTreasuryReconciliationCandidateSourceBindingsLedgerItem]
    custody: list[SavedTreasuryReconciliationCandidateSourceBindingsCustodyItem]

class SavedTreasuryReconciliationCandidateLedgerConservation(TypedDict):
    scope: Literal["SUPPLIED_IMMUTABLE_ENTRIES_ONLY"]
    ledgerVersion: Literal["treasury-ledger-v1", "treasury-ledger-v2"]
    conserved: Literal[True]
    commitment: str

class SavedTreasuryReconciliationCandidate(TypedDict):
    schemaVersion: Literal["treasury-ledger-custody-reconciliation-candidate-v1"]
    organizationId: str
    sourceCutoff: str
    status: Literal["REVIEW_CANDIDATE"]
    mappings: list[SavedTreasuryReconciliationCandidateMappingsItem]
    sourceBindings: SavedTreasuryReconciliationCandidateSourceBindings
    sourceHash: str
    candidateHash: str
    ledgerConservation: SavedTreasuryReconciliationCandidateLedgerConservation
    omittedLedgerEntryIds: list[str]
    omittedCustodyEvidenceIds: list[str]
    limitations: list[object]
    spendability: Literal["NOT_ESTABLISHED"]
    expenseCoverage: Literal["UNKNOWN"]
    financialAuthority: Literal[False]

class SavedTreasuryReconciliationAcknowledgmentVariant1(TypedDict):
    recordedBy: str
    recordedAt: str

class SavedTreasuryReconciliation(TypedDict):
    schemaVersion: Literal["treasury-reconciliation-draft-v1"]
    organizationId: str
    id: str
    sequence: str
    resourceVersion: str
    state: Literal["DRAFT", "ACKNOWLEDGED"]
    candidate: SavedTreasuryReconciliationCandidate
    createdBy: str
    createdAt: str
    recordedAt: str
    acknowledgment: Union[SavedTreasuryReconciliationAcknowledgmentVariant1, None]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryReconciliationWriteRecordCandidateMappingsItemLedger(TypedDict):
    recordId: str
    resourceVersion: str
    artifactHash: str

class TreasuryReconciliationWriteRecordCandidateMappingsItemCustody(TypedDict):
    evidenceId: str
    resourceVersion: str

class TreasuryReconciliationWriteRecordCandidateMappingsItemDeclaredSource(TypedDict):
    kind: Literal["SAFE", "VAULT", "EXTERNAL_MANAGER"]
    id: str

class TreasuryReconciliationWriteRecordCandidateMappingsItemUnit(TypedDict):
    chainId: int
    genesisHash: str
    asset: str
    decimals: int

class TreasuryReconciliationWriteRecordCandidateMappingsItemRelationship(TypedDict):
    id: str
    resourceVersion: str
    evidenceHash: str

class TreasuryReconciliationWriteRecordCandidateMappingsItemBlock(TypedDict):
    number: str
    hash: str
    timestamp: str

class TreasuryReconciliationWriteRecordCandidateMappingsItem(TypedDict):
    ledger: TreasuryReconciliationWriteRecordCandidateMappingsItemLedger
    custody: TreasuryReconciliationWriteRecordCandidateMappingsItemCustody
    capitalContainerId: str
    declaredCustodyLocationId: str
    declaredSource: TreasuryReconciliationWriteRecordCandidateMappingsItemDeclaredSource
    unit: TreasuryReconciliationWriteRecordCandidateMappingsItemUnit
    custodyAccount: str
    relationship: TreasuryReconciliationWriteRecordCandidateMappingsItemRelationship
    projectId: str
    block: TreasuryReconciliationWriteRecordCandidateMappingsItemBlock
    ledgerAmountAtomic: str
    observedCustodyAmountAtomic: str
    unallocatedCustodySurplusAtomic: str
    ledgerState: Literal["AVAILABLE", "DEPLOYED", "LOCKED", "AT_RISK", "FEE_GENERATING"]
    committedQuoteValuation: str
    obligationIds: list[str]
    disposition: Literal["PROPOSED_MAPPING_REQUIRES_ADMISSION"]

class TreasuryReconciliationWriteRecordCandidateSourceBindingsLedgerItem(TypedDict):
    recordId: str
    resourceVersion: str
    artifactHash: str

class TreasuryReconciliationWriteRecordCandidateSourceBindingsCustodyItem(TypedDict):
    evidenceId: str
    resourceVersion: str

class TreasuryReconciliationWriteRecordCandidateSourceBindings(TypedDict):
    ledger: list[TreasuryReconciliationWriteRecordCandidateSourceBindingsLedgerItem]
    custody: list[TreasuryReconciliationWriteRecordCandidateSourceBindingsCustodyItem]

class TreasuryReconciliationWriteRecordCandidateLedgerConservation(TypedDict):
    scope: Literal["SUPPLIED_IMMUTABLE_ENTRIES_ONLY"]
    ledgerVersion: Literal["treasury-ledger-v1", "treasury-ledger-v2"]
    conserved: Literal[True]
    commitment: str

class TreasuryReconciliationWriteRecordCandidate(TypedDict):
    schemaVersion: Literal["treasury-ledger-custody-reconciliation-candidate-v1"]
    organizationId: str
    sourceCutoff: str
    status: Literal["REVIEW_CANDIDATE"]
    mappings: list[TreasuryReconciliationWriteRecordCandidateMappingsItem]
    sourceBindings: TreasuryReconciliationWriteRecordCandidateSourceBindings
    sourceHash: str
    candidateHash: str
    ledgerConservation: TreasuryReconciliationWriteRecordCandidateLedgerConservation
    omittedLedgerEntryIds: list[str]
    omittedCustodyEvidenceIds: list[str]
    limitations: list[object]
    spendability: Literal["NOT_ESTABLISHED"]
    expenseCoverage: Literal["UNKNOWN"]
    financialAuthority: Literal[False]

class TreasuryReconciliationWriteRecordAcknowledgmentVariant1(TypedDict):
    recordedBy: str
    recordedAt: str

class TreasuryReconciliationWriteRecord(TypedDict):
    schemaVersion: Literal["treasury-reconciliation-draft-v1"]
    organizationId: str
    id: str
    sequence: str
    resourceVersion: str
    state: Literal["DRAFT", "ACKNOWLEDGED"]
    candidate: TreasuryReconciliationWriteRecordCandidate
    createdBy: str
    createdAt: str
    recordedAt: str
    acknowledgment: Union[TreasuryReconciliationWriteRecordAcknowledgmentVariant1, None]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryReconciliationWrite(TypedDict):
    record: TreasuryReconciliationWriteRecord
    replayed: bool

class TreasuryReconciliationListItemsItemCandidateMappingsItemLedger(TypedDict):
    recordId: str
    resourceVersion: str
    artifactHash: str

class TreasuryReconciliationListItemsItemCandidateMappingsItemCustody(TypedDict):
    evidenceId: str
    resourceVersion: str

class TreasuryReconciliationListItemsItemCandidateMappingsItemDeclaredSource(TypedDict):
    kind: Literal["SAFE", "VAULT", "EXTERNAL_MANAGER"]
    id: str

class TreasuryReconciliationListItemsItemCandidateMappingsItemUnit(TypedDict):
    chainId: int
    genesisHash: str
    asset: str
    decimals: int

class TreasuryReconciliationListItemsItemCandidateMappingsItemRelationship(TypedDict):
    id: str
    resourceVersion: str
    evidenceHash: str

class TreasuryReconciliationListItemsItemCandidateMappingsItemBlock(TypedDict):
    number: str
    hash: str
    timestamp: str

class TreasuryReconciliationListItemsItemCandidateMappingsItem(TypedDict):
    ledger: TreasuryReconciliationListItemsItemCandidateMappingsItemLedger
    custody: TreasuryReconciliationListItemsItemCandidateMappingsItemCustody
    capitalContainerId: str
    declaredCustodyLocationId: str
    declaredSource: TreasuryReconciliationListItemsItemCandidateMappingsItemDeclaredSource
    unit: TreasuryReconciliationListItemsItemCandidateMappingsItemUnit
    custodyAccount: str
    relationship: TreasuryReconciliationListItemsItemCandidateMappingsItemRelationship
    projectId: str
    block: TreasuryReconciliationListItemsItemCandidateMappingsItemBlock
    ledgerAmountAtomic: str
    observedCustodyAmountAtomic: str
    unallocatedCustodySurplusAtomic: str
    ledgerState: Literal["AVAILABLE", "DEPLOYED", "LOCKED", "AT_RISK", "FEE_GENERATING"]
    committedQuoteValuation: str
    obligationIds: list[str]
    disposition: Literal["PROPOSED_MAPPING_REQUIRES_ADMISSION"]

class TreasuryReconciliationListItemsItemCandidateSourceBindingsLedgerItem(TypedDict):
    recordId: str
    resourceVersion: str
    artifactHash: str

class TreasuryReconciliationListItemsItemCandidateSourceBindingsCustodyItem(TypedDict):
    evidenceId: str
    resourceVersion: str

class TreasuryReconciliationListItemsItemCandidateSourceBindings(TypedDict):
    ledger: list[TreasuryReconciliationListItemsItemCandidateSourceBindingsLedgerItem]
    custody: list[TreasuryReconciliationListItemsItemCandidateSourceBindingsCustodyItem]

class TreasuryReconciliationListItemsItemCandidateLedgerConservation(TypedDict):
    scope: Literal["SUPPLIED_IMMUTABLE_ENTRIES_ONLY"]
    ledgerVersion: Literal["treasury-ledger-v1", "treasury-ledger-v2"]
    conserved: Literal[True]
    commitment: str

class TreasuryReconciliationListItemsItemCandidate(TypedDict):
    schemaVersion: Literal["treasury-ledger-custody-reconciliation-candidate-v1"]
    organizationId: str
    sourceCutoff: str
    status: Literal["REVIEW_CANDIDATE"]
    mappings: list[TreasuryReconciliationListItemsItemCandidateMappingsItem]
    sourceBindings: TreasuryReconciliationListItemsItemCandidateSourceBindings
    sourceHash: str
    candidateHash: str
    ledgerConservation: TreasuryReconciliationListItemsItemCandidateLedgerConservation
    omittedLedgerEntryIds: list[str]
    omittedCustodyEvidenceIds: list[str]
    limitations: list[object]
    spendability: Literal["NOT_ESTABLISHED"]
    expenseCoverage: Literal["UNKNOWN"]
    financialAuthority: Literal[False]

class TreasuryReconciliationListItemsItemAcknowledgmentVariant1(TypedDict):
    recordedBy: str
    recordedAt: str

class TreasuryReconciliationListItemsItem(TypedDict):
    schemaVersion: Literal["treasury-reconciliation-draft-v1"]
    organizationId: str
    id: str
    sequence: str
    resourceVersion: str
    state: Literal["DRAFT", "ACKNOWLEDGED"]
    candidate: TreasuryReconciliationListItemsItemCandidate
    createdBy: str
    createdAt: str
    recordedAt: str
    acknowledgment: Union[TreasuryReconciliationListItemsItemAcknowledgmentVariant1, None]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryReconciliationList(TypedDict):
    items: list[TreasuryReconciliationListItemsItem]
    nextCursor: Union[str, None]

class TreasuryReconciliationHistoryItemsItemCandidateMappingsItemLedger(TypedDict):
    recordId: str
    resourceVersion: str
    artifactHash: str

class TreasuryReconciliationHistoryItemsItemCandidateMappingsItemCustody(TypedDict):
    evidenceId: str
    resourceVersion: str

class TreasuryReconciliationHistoryItemsItemCandidateMappingsItemDeclaredSource(TypedDict):
    kind: Literal["SAFE", "VAULT", "EXTERNAL_MANAGER"]
    id: str

class TreasuryReconciliationHistoryItemsItemCandidateMappingsItemUnit(TypedDict):
    chainId: int
    genesisHash: str
    asset: str
    decimals: int

class TreasuryReconciliationHistoryItemsItemCandidateMappingsItemRelationship(TypedDict):
    id: str
    resourceVersion: str
    evidenceHash: str

class TreasuryReconciliationHistoryItemsItemCandidateMappingsItemBlock(TypedDict):
    number: str
    hash: str
    timestamp: str

class TreasuryReconciliationHistoryItemsItemCandidateMappingsItem(TypedDict):
    ledger: TreasuryReconciliationHistoryItemsItemCandidateMappingsItemLedger
    custody: TreasuryReconciliationHistoryItemsItemCandidateMappingsItemCustody
    capitalContainerId: str
    declaredCustodyLocationId: str
    declaredSource: TreasuryReconciliationHistoryItemsItemCandidateMappingsItemDeclaredSource
    unit: TreasuryReconciliationHistoryItemsItemCandidateMappingsItemUnit
    custodyAccount: str
    relationship: TreasuryReconciliationHistoryItemsItemCandidateMappingsItemRelationship
    projectId: str
    block: TreasuryReconciliationHistoryItemsItemCandidateMappingsItemBlock
    ledgerAmountAtomic: str
    observedCustodyAmountAtomic: str
    unallocatedCustodySurplusAtomic: str
    ledgerState: Literal["AVAILABLE", "DEPLOYED", "LOCKED", "AT_RISK", "FEE_GENERATING"]
    committedQuoteValuation: str
    obligationIds: list[str]
    disposition: Literal["PROPOSED_MAPPING_REQUIRES_ADMISSION"]

class TreasuryReconciliationHistoryItemsItemCandidateSourceBindingsLedgerItem(TypedDict):
    recordId: str
    resourceVersion: str
    artifactHash: str

class TreasuryReconciliationHistoryItemsItemCandidateSourceBindingsCustodyItem(TypedDict):
    evidenceId: str
    resourceVersion: str

class TreasuryReconciliationHistoryItemsItemCandidateSourceBindings(TypedDict):
    ledger: list[TreasuryReconciliationHistoryItemsItemCandidateSourceBindingsLedgerItem]
    custody: list[TreasuryReconciliationHistoryItemsItemCandidateSourceBindingsCustodyItem]

class TreasuryReconciliationHistoryItemsItemCandidateLedgerConservation(TypedDict):
    scope: Literal["SUPPLIED_IMMUTABLE_ENTRIES_ONLY"]
    ledgerVersion: Literal["treasury-ledger-v1", "treasury-ledger-v2"]
    conserved: Literal[True]
    commitment: str

class TreasuryReconciliationHistoryItemsItemCandidate(TypedDict):
    schemaVersion: Literal["treasury-ledger-custody-reconciliation-candidate-v1"]
    organizationId: str
    sourceCutoff: str
    status: Literal["REVIEW_CANDIDATE"]
    mappings: list[TreasuryReconciliationHistoryItemsItemCandidateMappingsItem]
    sourceBindings: TreasuryReconciliationHistoryItemsItemCandidateSourceBindings
    sourceHash: str
    candidateHash: str
    ledgerConservation: TreasuryReconciliationHistoryItemsItemCandidateLedgerConservation
    omittedLedgerEntryIds: list[str]
    omittedCustodyEvidenceIds: list[str]
    limitations: list[object]
    spendability: Literal["NOT_ESTABLISHED"]
    expenseCoverage: Literal["UNKNOWN"]
    financialAuthority: Literal[False]

class TreasuryReconciliationHistoryItemsItemAcknowledgmentVariant1(TypedDict):
    recordedBy: str
    recordedAt: str

class TreasuryReconciliationHistoryItemsItem(TypedDict):
    schemaVersion: Literal["treasury-reconciliation-draft-v1"]
    organizationId: str
    id: str
    sequence: str
    resourceVersion: str
    state: Literal["DRAFT", "ACKNOWLEDGED"]
    candidate: TreasuryReconciliationHistoryItemsItemCandidate
    createdBy: str
    createdAt: str
    recordedAt: str
    acknowledgment: Union[TreasuryReconciliationHistoryItemsItemAcknowledgmentVariant1, None]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryReconciliationHistory(TypedDict):
    items: list[TreasuryReconciliationHistoryItemsItem]
    nextCursor: Union[str, None]

class TreasuryAssumptionsCreateReconciliation(TypedDict):
    id: str
    resourceVersion: str

class TreasuryAssumptionsCreateAssumptionsObligationsItemInstallmentsItem(TypedDict):
    id: str
    dueDay: str
    amountAtomic: str

class TreasuryAssumptionsCreateAssumptionsObligationsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    totalAmountAtomic: str
    installments: list[TreasuryAssumptionsCreateAssumptionsObligationsItemInstallmentsItem]

class TreasuryAssumptionsCreateAssumptionsConditionalInflowsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    expectedDay: str
    amountAtomic: str
    condition: str

class TreasuryAssumptionsCreateAssumptionsAllocationsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    day: str
    amountAtomic: str

class TreasuryAssumptionsCreateAssumptionsLedgerObligationCoverageItem(TypedDict):
    ledgerObligationId: str
    relation: Literal["SCHEDULED_HERE", "DECLARED_ALREADY_DEDUCTED", "UNRESOLVED"]
    scheduleIds: list[str]
    note: str

class TreasuryAssumptionsCreateAssumptionsExpenseCoverage(TypedDict):
    declaration: Literal["DECLARED_COMPLETE", "DECLARED_PARTIAL", "UNKNOWN"]
    omittedCategories: list[str]
    note: str

class TreasuryAssumptionsCreateAssumptions(TypedDict):
    title: str
    obligations: list[TreasuryAssumptionsCreateAssumptionsObligationsItem]
    conditionalInflows: list[TreasuryAssumptionsCreateAssumptionsConditionalInflowsItem]
    allocations: list[TreasuryAssumptionsCreateAssumptionsAllocationsItem]
    ledgerObligationCoverage: list[TreasuryAssumptionsCreateAssumptionsLedgerObligationCoverageItem]
    expenseCoverage: TreasuryAssumptionsCreateAssumptionsExpenseCoverage

class TreasuryAssumptionsCreate(TypedDict):
    reconciliation: TreasuryAssumptionsCreateReconciliation
    ledgerEntryIds: list[str]
    assumptions: TreasuryAssumptionsCreateAssumptions

class TreasuryAssumptionsRevisionAssumptionsObligationsItemInstallmentsItem(TypedDict):
    id: str
    dueDay: str
    amountAtomic: str

class TreasuryAssumptionsRevisionAssumptionsObligationsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    totalAmountAtomic: str
    installments: list[TreasuryAssumptionsRevisionAssumptionsObligationsItemInstallmentsItem]

class TreasuryAssumptionsRevisionAssumptionsConditionalInflowsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    expectedDay: str
    amountAtomic: str
    condition: str

class TreasuryAssumptionsRevisionAssumptionsAllocationsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    day: str
    amountAtomic: str

class TreasuryAssumptionsRevisionAssumptionsLedgerObligationCoverageItem(TypedDict):
    ledgerObligationId: str
    relation: Literal["SCHEDULED_HERE", "DECLARED_ALREADY_DEDUCTED", "UNRESOLVED"]
    scheduleIds: list[str]
    note: str

class TreasuryAssumptionsRevisionAssumptionsExpenseCoverage(TypedDict):
    declaration: Literal["DECLARED_COMPLETE", "DECLARED_PARTIAL", "UNKNOWN"]
    omittedCategories: list[str]
    note: str

class TreasuryAssumptionsRevisionAssumptions(TypedDict):
    title: str
    obligations: list[TreasuryAssumptionsRevisionAssumptionsObligationsItem]
    conditionalInflows: list[TreasuryAssumptionsRevisionAssumptionsConditionalInflowsItem]
    allocations: list[TreasuryAssumptionsRevisionAssumptionsAllocationsItem]
    ledgerObligationCoverage: list[TreasuryAssumptionsRevisionAssumptionsLedgerObligationCoverageItem]
    expenseCoverage: TreasuryAssumptionsRevisionAssumptionsExpenseCoverage

class TreasuryAssumptionsRevision(TypedDict):
    assumptions: TreasuryAssumptionsRevisionAssumptions

class TreasuryAssumptionsReconciliation(TypedDict):
    id: str
    resourceVersion: str

class TreasuryAssumptionsUnit(TypedDict):
    chainId: int
    genesisHash: str
    asset: str
    decimals: int

class TreasuryAssumptionsAssumptionsObligationsItemInstallmentsItem(TypedDict):
    id: str
    dueDay: str
    amountAtomic: str

class TreasuryAssumptionsAssumptionsObligationsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    totalAmountAtomic: str
    installments: list[TreasuryAssumptionsAssumptionsObligationsItemInstallmentsItem]

class TreasuryAssumptionsAssumptionsConditionalInflowsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    expectedDay: str
    amountAtomic: str
    condition: str

class TreasuryAssumptionsAssumptionsAllocationsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    day: str
    amountAtomic: str

class TreasuryAssumptionsAssumptionsLedgerObligationCoverageItem(TypedDict):
    ledgerObligationId: str
    relation: Literal["SCHEDULED_HERE", "DECLARED_ALREADY_DEDUCTED", "UNRESOLVED"]
    scheduleIds: list[str]
    note: str

class TreasuryAssumptionsAssumptionsExpenseCoverage(TypedDict):
    declaration: Literal["DECLARED_COMPLETE", "DECLARED_PARTIAL", "UNKNOWN"]
    omittedCategories: list[str]
    note: str

class TreasuryAssumptionsAssumptions(TypedDict):
    title: str
    obligations: list[TreasuryAssumptionsAssumptionsObligationsItem]
    conditionalInflows: list[TreasuryAssumptionsAssumptionsConditionalInflowsItem]
    allocations: list[TreasuryAssumptionsAssumptionsAllocationsItem]
    ledgerObligationCoverage: list[TreasuryAssumptionsAssumptionsLedgerObligationCoverageItem]
    expenseCoverage: TreasuryAssumptionsAssumptionsExpenseCoverage

class TreasuryAssumptions(TypedDict):
    schemaVersion: Literal["treasury-dated-assumptions-v1"]
    organizationId: str
    id: str
    sequence: str
    resourceVersion: str
    reconciliation: TreasuryAssumptionsReconciliation
    ledgerEntryIds: list[str]
    unit: TreasuryAssumptionsUnit
    assumptions: TreasuryAssumptionsAssumptions
    provenance: Literal["ISSUER_DECLARED_UNVERIFIED"]
    verifiedExpenseCoverage: Literal["UNKNOWN"]
    createdBy: str
    createdAt: str
    recordedBy: str
    recordedAt: str
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryAssumptionsWriteRecordReconciliation(TypedDict):
    id: str
    resourceVersion: str

class TreasuryAssumptionsWriteRecordUnit(TypedDict):
    chainId: int
    genesisHash: str
    asset: str
    decimals: int

class TreasuryAssumptionsWriteRecordAssumptionsObligationsItemInstallmentsItem(TypedDict):
    id: str
    dueDay: str
    amountAtomic: str

class TreasuryAssumptionsWriteRecordAssumptionsObligationsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    totalAmountAtomic: str
    installments: list[TreasuryAssumptionsWriteRecordAssumptionsObligationsItemInstallmentsItem]

class TreasuryAssumptionsWriteRecordAssumptionsConditionalInflowsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    expectedDay: str
    amountAtomic: str
    condition: str

class TreasuryAssumptionsWriteRecordAssumptionsAllocationsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    day: str
    amountAtomic: str

class TreasuryAssumptionsWriteRecordAssumptionsLedgerObligationCoverageItem(TypedDict):
    ledgerObligationId: str
    relation: Literal["SCHEDULED_HERE", "DECLARED_ALREADY_DEDUCTED", "UNRESOLVED"]
    scheduleIds: list[str]
    note: str

class TreasuryAssumptionsWriteRecordAssumptionsExpenseCoverage(TypedDict):
    declaration: Literal["DECLARED_COMPLETE", "DECLARED_PARTIAL", "UNKNOWN"]
    omittedCategories: list[str]
    note: str

class TreasuryAssumptionsWriteRecordAssumptions(TypedDict):
    title: str
    obligations: list[TreasuryAssumptionsWriteRecordAssumptionsObligationsItem]
    conditionalInflows: list[TreasuryAssumptionsWriteRecordAssumptionsConditionalInflowsItem]
    allocations: list[TreasuryAssumptionsWriteRecordAssumptionsAllocationsItem]
    ledgerObligationCoverage: list[TreasuryAssumptionsWriteRecordAssumptionsLedgerObligationCoverageItem]
    expenseCoverage: TreasuryAssumptionsWriteRecordAssumptionsExpenseCoverage

class TreasuryAssumptionsWriteRecord(TypedDict):
    schemaVersion: Literal["treasury-dated-assumptions-v1"]
    organizationId: str
    id: str
    sequence: str
    resourceVersion: str
    reconciliation: TreasuryAssumptionsWriteRecordReconciliation
    ledgerEntryIds: list[str]
    unit: TreasuryAssumptionsWriteRecordUnit
    assumptions: TreasuryAssumptionsWriteRecordAssumptions
    provenance: Literal["ISSUER_DECLARED_UNVERIFIED"]
    verifiedExpenseCoverage: Literal["UNKNOWN"]
    createdBy: str
    createdAt: str
    recordedBy: str
    recordedAt: str
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryAssumptionsWrite(TypedDict):
    record: TreasuryAssumptionsWriteRecord
    replayed: bool

class TreasuryAssumptionsListItemsItemReconciliation(TypedDict):
    id: str
    resourceVersion: str

class TreasuryAssumptionsListItemsItemUnit(TypedDict):
    chainId: int
    genesisHash: str
    asset: str
    decimals: int

class TreasuryAssumptionsListItemsItemAssumptionsObligationsItemInstallmentsItem(TypedDict):
    id: str
    dueDay: str
    amountAtomic: str

class TreasuryAssumptionsListItemsItemAssumptionsObligationsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    totalAmountAtomic: str
    installments: list[TreasuryAssumptionsListItemsItemAssumptionsObligationsItemInstallmentsItem]

class TreasuryAssumptionsListItemsItemAssumptionsConditionalInflowsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    expectedDay: str
    amountAtomic: str
    condition: str

class TreasuryAssumptionsListItemsItemAssumptionsAllocationsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    day: str
    amountAtomic: str

class TreasuryAssumptionsListItemsItemAssumptionsLedgerObligationCoverageItem(TypedDict):
    ledgerObligationId: str
    relation: Literal["SCHEDULED_HERE", "DECLARED_ALREADY_DEDUCTED", "UNRESOLVED"]
    scheduleIds: list[str]
    note: str

class TreasuryAssumptionsListItemsItemAssumptionsExpenseCoverage(TypedDict):
    declaration: Literal["DECLARED_COMPLETE", "DECLARED_PARTIAL", "UNKNOWN"]
    omittedCategories: list[str]
    note: str

class TreasuryAssumptionsListItemsItemAssumptions(TypedDict):
    title: str
    obligations: list[TreasuryAssumptionsListItemsItemAssumptionsObligationsItem]
    conditionalInflows: list[TreasuryAssumptionsListItemsItemAssumptionsConditionalInflowsItem]
    allocations: list[TreasuryAssumptionsListItemsItemAssumptionsAllocationsItem]
    ledgerObligationCoverage: list[TreasuryAssumptionsListItemsItemAssumptionsLedgerObligationCoverageItem]
    expenseCoverage: TreasuryAssumptionsListItemsItemAssumptionsExpenseCoverage

class TreasuryAssumptionsListItemsItem(TypedDict):
    schemaVersion: Literal["treasury-dated-assumptions-v1"]
    organizationId: str
    id: str
    sequence: str
    resourceVersion: str
    reconciliation: TreasuryAssumptionsListItemsItemReconciliation
    ledgerEntryIds: list[str]
    unit: TreasuryAssumptionsListItemsItemUnit
    assumptions: TreasuryAssumptionsListItemsItemAssumptions
    provenance: Literal["ISSUER_DECLARED_UNVERIFIED"]
    verifiedExpenseCoverage: Literal["UNKNOWN"]
    createdBy: str
    createdAt: str
    recordedBy: str
    recordedAt: str
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryAssumptionsList(TypedDict):
    items: list[TreasuryAssumptionsListItemsItem]
    nextCursor: Union[str, None]

class TreasuryAssumptionsHistoryItemsItemReconciliation(TypedDict):
    id: str
    resourceVersion: str

class TreasuryAssumptionsHistoryItemsItemUnit(TypedDict):
    chainId: int
    genesisHash: str
    asset: str
    decimals: int

class TreasuryAssumptionsHistoryItemsItemAssumptionsObligationsItemInstallmentsItem(TypedDict):
    id: str
    dueDay: str
    amountAtomic: str

class TreasuryAssumptionsHistoryItemsItemAssumptionsObligationsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    totalAmountAtomic: str
    installments: list[TreasuryAssumptionsHistoryItemsItemAssumptionsObligationsItemInstallmentsItem]

class TreasuryAssumptionsHistoryItemsItemAssumptionsConditionalInflowsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    expectedDay: str
    amountAtomic: str
    condition: str

class TreasuryAssumptionsHistoryItemsItemAssumptionsAllocationsItem(TypedDict):
    id: str
    economicKey: str
    label: str
    day: str
    amountAtomic: str

class TreasuryAssumptionsHistoryItemsItemAssumptionsLedgerObligationCoverageItem(TypedDict):
    ledgerObligationId: str
    relation: Literal["SCHEDULED_HERE", "DECLARED_ALREADY_DEDUCTED", "UNRESOLVED"]
    scheduleIds: list[str]
    note: str

class TreasuryAssumptionsHistoryItemsItemAssumptionsExpenseCoverage(TypedDict):
    declaration: Literal["DECLARED_COMPLETE", "DECLARED_PARTIAL", "UNKNOWN"]
    omittedCategories: list[str]
    note: str

class TreasuryAssumptionsHistoryItemsItemAssumptions(TypedDict):
    title: str
    obligations: list[TreasuryAssumptionsHistoryItemsItemAssumptionsObligationsItem]
    conditionalInflows: list[TreasuryAssumptionsHistoryItemsItemAssumptionsConditionalInflowsItem]
    allocations: list[TreasuryAssumptionsHistoryItemsItemAssumptionsAllocationsItem]
    ledgerObligationCoverage: list[TreasuryAssumptionsHistoryItemsItemAssumptionsLedgerObligationCoverageItem]
    expenseCoverage: TreasuryAssumptionsHistoryItemsItemAssumptionsExpenseCoverage

class TreasuryAssumptionsHistoryItemsItem(TypedDict):
    schemaVersion: Literal["treasury-dated-assumptions-v1"]
    organizationId: str
    id: str
    sequence: str
    resourceVersion: str
    reconciliation: TreasuryAssumptionsHistoryItemsItemReconciliation
    ledgerEntryIds: list[str]
    unit: TreasuryAssumptionsHistoryItemsItemUnit
    assumptions: TreasuryAssumptionsHistoryItemsItemAssumptions
    provenance: Literal["ISSUER_DECLARED_UNVERIFIED"]
    verifiedExpenseCoverage: Literal["UNKNOWN"]
    createdBy: str
    createdAt: str
    recordedBy: str
    recordedAt: str
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryAssumptionsHistory(TypedDict):
    items: list[TreasuryAssumptionsHistoryItemsItem]
    nextCursor: Union[str, None]

class TreasuryProjectionCreateAssumptions(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionCreateRestrictionsItem(TypedDict):
    ledgerEntryId: str
    restrictedAmountAtomic: str
    reason: str

class TreasuryProjectionCreate(TypedDict):
    assumptions: TreasuryProjectionCreateAssumptions
    throughDay: str
    restrictions: list[TreasuryProjectionCreateRestrictionsItem]
    confirmation: Literal["UNPAID_SCHEDULES_AND_RESTRICTIONS_EXCLUDE_THEM"]

class TreasuryProjectionRequestAssumptions(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionRequestRestrictionsItem(TypedDict):
    ledgerEntryId: str
    restrictedAmountAtomic: str
    reason: str

class TreasuryProjectionRequest(TypedDict):
    assumptions: TreasuryProjectionRequestAssumptions
    throughDay: str
    restrictions: list[TreasuryProjectionRequestRestrictionsItem]
    confirmation: Literal["UNPAID_SCHEDULES_AND_RESTRICTIONS_EXCLUDE_THEM"]

class TreasuryProjectionResultAssumptions(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionResultReconciliation(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionResultRequestAssumptions(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionResultRequestRestrictionsItem(TypedDict):
    ledgerEntryId: str
    restrictedAmountAtomic: str
    reason: str

class TreasuryProjectionResultRequest(TypedDict):
    assumptions: TreasuryProjectionResultRequestAssumptions
    throughDay: str
    restrictions: list[TreasuryProjectionResultRequestRestrictionsItem]
    confirmation: Literal["UNPAID_SCHEDULES_AND_RESTRICTIONS_EXCLUDE_THEM"]

class TreasuryProjectionResultSourceBlock(TypedDict):
    number: str
    hash: str
    timestamp: str

class TreasuryProjectionResultUnit(TypedDict):
    chainId: int
    genesisHash: str
    asset: str
    decimals: int

class TreasuryProjectionResultOpening(TypedDict):
    availableMappedAtomic: str
    declaredRestrictedAtomic: str
    scenarioBalanceAtomic: str

class TreasuryProjectionResultSelectedMappingsItem(TypedDict):
    ledgerEntryId: str
    ledgerResourceVersion: str
    custodyEvidenceId: str
    custodyResourceVersion: str
    ledgerState: Literal["AVAILABLE", "DEPLOYED", "LOCKED", "AT_RISK", "FEE_GENERATING"]
    ledgerAmountAtomic: str
    declaredRestrictedAtomic: str
    restrictionReason: str
    includedInOpening: bool
    disposition: Literal["AVAILABLE_DECLARED_SCENARIO", "NON_AVAILABLE_EXCLUDED"]

class TreasuryProjectionResultTimelineItem(TypedDict):
    day: str
    actualInflowsAtomic: Literal["0"]
    obligationsAtomic: str
    allocationsAtomic: str
    conditionalInflowsAtomic: str
    closingBaselineAtomic: str
    cumulativeConditionalAtomic: str
    closingConditionalScenarioAtomic: str

class TreasuryProjectionResultExcludedEventsItem(TypedDict):
    id: str
    kind: Literal["OBLIGATION", "ALLOCATION", "CONDITIONAL_INFLOW"]
    day: str
    amountAtomic: str
    reason: Literal["AFTER_HORIZON"]

class TreasuryProjectionResultDeclaredExpenseCoverage(TypedDict):
    declaration: Literal["DECLARED_COMPLETE", "DECLARED_PARTIAL", "UNKNOWN"]
    omittedCategories: list[str]
    note: str

class TreasuryProjectionResult(TypedDict):
    schemaVersion: Literal["treasury-snapshot-projection-model-v1"]
    organizationId: str
    assumptions: TreasuryProjectionResultAssumptions
    reconciliation: TreasuryProjectionResultReconciliation
    request: TreasuryProjectionResultRequest
    sourceBlock: TreasuryProjectionResultSourceBlock
    sourceCutoff: str
    unit: TreasuryProjectionResultUnit
    openingDay: str
    throughDay: str
    opening: TreasuryProjectionResultOpening
    selectedMappings: list[TreasuryProjectionResultSelectedMappingsItem]
    timeline: list[TreasuryProjectionResultTimelineItem]
    excludedEvents: list[TreasuryProjectionResultExcludedEventsItem]
    firstShortfallDay: Union[str, None]
    minimumBaselineAtomic: str
    closingBaselineAtomic: str
    conditionalInflowsAtomic: str
    closingConditionalScenarioAtomic: str
    declaredExpenseCoverage: TreasuryProjectionResultDeclaredExpenseCoverage
    provenance: Literal["DECLARED_SCENARIO"]
    verifiedExpenseCoverage: Literal["UNKNOWN"]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]
    limitations: list[Literal["ISSUER_DECLARATIONS_ARE_NOT_VERIFIED_SPENDABILITY", "EXPENSE_COMPLETENESS_REMAINS_UNKNOWN", "SNAPSHOT_DAY_UNPAID_OUTFLOWS_ARE_INCLUDED", "DAILY_BUCKETS_DO_NOT_ESTABLISH_INTRADAY_SOLVENCY", "CONDITIONAL_INCOME_IS_NOT_SETTLED_CASH", "UNALLOCATED_CUSTODY_SURPLUS_IS_EXCLUDED", "NON_AVAILABLE_LEDGER_BALANCES_ARE_EXCLUDED", "RESTRICTIONS_ARE_DECLARED_SEPARATELY_FROM_SCHEDULES", "HISTORICAL_SOURCES_DO_NOT_ESTABLISH_CURRENT_APPLICABILITY"]]
    modelHash: str

class TreasuryProjection(TypedDict):
    schemaVersion: Literal["treasury-declared-projection-v1"]
    organizationId: str
    id: str
    resourceVersion: str
    request: TreasuryProjectionRequest
    result: TreasuryProjectionResult
    sourceHash: str
    createdBy: str
    createdAt: str
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryProjectionWriteRecordRequestAssumptions(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionWriteRecordRequestRestrictionsItem(TypedDict):
    ledgerEntryId: str
    restrictedAmountAtomic: str
    reason: str

class TreasuryProjectionWriteRecordRequest(TypedDict):
    assumptions: TreasuryProjectionWriteRecordRequestAssumptions
    throughDay: str
    restrictions: list[TreasuryProjectionWriteRecordRequestRestrictionsItem]
    confirmation: Literal["UNPAID_SCHEDULES_AND_RESTRICTIONS_EXCLUDE_THEM"]

class TreasuryProjectionWriteRecordResultAssumptions(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionWriteRecordResultReconciliation(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionWriteRecordResultRequestAssumptions(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionWriteRecordResultRequestRestrictionsItem(TypedDict):
    ledgerEntryId: str
    restrictedAmountAtomic: str
    reason: str

class TreasuryProjectionWriteRecordResultRequest(TypedDict):
    assumptions: TreasuryProjectionWriteRecordResultRequestAssumptions
    throughDay: str
    restrictions: list[TreasuryProjectionWriteRecordResultRequestRestrictionsItem]
    confirmation: Literal["UNPAID_SCHEDULES_AND_RESTRICTIONS_EXCLUDE_THEM"]

class TreasuryProjectionWriteRecordResultSourceBlock(TypedDict):
    number: str
    hash: str
    timestamp: str

class TreasuryProjectionWriteRecordResultUnit(TypedDict):
    chainId: int
    genesisHash: str
    asset: str
    decimals: int

class TreasuryProjectionWriteRecordResultOpening(TypedDict):
    availableMappedAtomic: str
    declaredRestrictedAtomic: str
    scenarioBalanceAtomic: str

class TreasuryProjectionWriteRecordResultSelectedMappingsItem(TypedDict):
    ledgerEntryId: str
    ledgerResourceVersion: str
    custodyEvidenceId: str
    custodyResourceVersion: str
    ledgerState: Literal["AVAILABLE", "DEPLOYED", "LOCKED", "AT_RISK", "FEE_GENERATING"]
    ledgerAmountAtomic: str
    declaredRestrictedAtomic: str
    restrictionReason: str
    includedInOpening: bool
    disposition: Literal["AVAILABLE_DECLARED_SCENARIO", "NON_AVAILABLE_EXCLUDED"]

class TreasuryProjectionWriteRecordResultTimelineItem(TypedDict):
    day: str
    actualInflowsAtomic: Literal["0"]
    obligationsAtomic: str
    allocationsAtomic: str
    conditionalInflowsAtomic: str
    closingBaselineAtomic: str
    cumulativeConditionalAtomic: str
    closingConditionalScenarioAtomic: str

class TreasuryProjectionWriteRecordResultExcludedEventsItem(TypedDict):
    id: str
    kind: Literal["OBLIGATION", "ALLOCATION", "CONDITIONAL_INFLOW"]
    day: str
    amountAtomic: str
    reason: Literal["AFTER_HORIZON"]

class TreasuryProjectionWriteRecordResultDeclaredExpenseCoverage(TypedDict):
    declaration: Literal["DECLARED_COMPLETE", "DECLARED_PARTIAL", "UNKNOWN"]
    omittedCategories: list[str]
    note: str

class TreasuryProjectionWriteRecordResult(TypedDict):
    schemaVersion: Literal["treasury-snapshot-projection-model-v1"]
    organizationId: str
    assumptions: TreasuryProjectionWriteRecordResultAssumptions
    reconciliation: TreasuryProjectionWriteRecordResultReconciliation
    request: TreasuryProjectionWriteRecordResultRequest
    sourceBlock: TreasuryProjectionWriteRecordResultSourceBlock
    sourceCutoff: str
    unit: TreasuryProjectionWriteRecordResultUnit
    openingDay: str
    throughDay: str
    opening: TreasuryProjectionWriteRecordResultOpening
    selectedMappings: list[TreasuryProjectionWriteRecordResultSelectedMappingsItem]
    timeline: list[TreasuryProjectionWriteRecordResultTimelineItem]
    excludedEvents: list[TreasuryProjectionWriteRecordResultExcludedEventsItem]
    firstShortfallDay: Union[str, None]
    minimumBaselineAtomic: str
    closingBaselineAtomic: str
    conditionalInflowsAtomic: str
    closingConditionalScenarioAtomic: str
    declaredExpenseCoverage: TreasuryProjectionWriteRecordResultDeclaredExpenseCoverage
    provenance: Literal["DECLARED_SCENARIO"]
    verifiedExpenseCoverage: Literal["UNKNOWN"]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]
    limitations: list[Literal["ISSUER_DECLARATIONS_ARE_NOT_VERIFIED_SPENDABILITY", "EXPENSE_COMPLETENESS_REMAINS_UNKNOWN", "SNAPSHOT_DAY_UNPAID_OUTFLOWS_ARE_INCLUDED", "DAILY_BUCKETS_DO_NOT_ESTABLISH_INTRADAY_SOLVENCY", "CONDITIONAL_INCOME_IS_NOT_SETTLED_CASH", "UNALLOCATED_CUSTODY_SURPLUS_IS_EXCLUDED", "NON_AVAILABLE_LEDGER_BALANCES_ARE_EXCLUDED", "RESTRICTIONS_ARE_DECLARED_SEPARATELY_FROM_SCHEDULES", "HISTORICAL_SOURCES_DO_NOT_ESTABLISH_CURRENT_APPLICABILITY"]]
    modelHash: str

class TreasuryProjectionWriteRecord(TypedDict):
    schemaVersion: Literal["treasury-declared-projection-v1"]
    organizationId: str
    id: str
    resourceVersion: str
    request: TreasuryProjectionWriteRecordRequest
    result: TreasuryProjectionWriteRecordResult
    sourceHash: str
    createdBy: str
    createdAt: str
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryProjectionWrite(TypedDict):
    record: TreasuryProjectionWriteRecord
    replayed: bool

class TreasuryProjectionListItemsItemRequestAssumptions(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionListItemsItemRequestRestrictionsItem(TypedDict):
    ledgerEntryId: str
    restrictedAmountAtomic: str
    reason: str

class TreasuryProjectionListItemsItemRequest(TypedDict):
    assumptions: TreasuryProjectionListItemsItemRequestAssumptions
    throughDay: str
    restrictions: list[TreasuryProjectionListItemsItemRequestRestrictionsItem]
    confirmation: Literal["UNPAID_SCHEDULES_AND_RESTRICTIONS_EXCLUDE_THEM"]

class TreasuryProjectionListItemsItemResultAssumptions(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionListItemsItemResultReconciliation(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionListItemsItemResultRequestAssumptions(TypedDict):
    id: str
    resourceVersion: str

class TreasuryProjectionListItemsItemResultRequestRestrictionsItem(TypedDict):
    ledgerEntryId: str
    restrictedAmountAtomic: str
    reason: str

class TreasuryProjectionListItemsItemResultRequest(TypedDict):
    assumptions: TreasuryProjectionListItemsItemResultRequestAssumptions
    throughDay: str
    restrictions: list[TreasuryProjectionListItemsItemResultRequestRestrictionsItem]
    confirmation: Literal["UNPAID_SCHEDULES_AND_RESTRICTIONS_EXCLUDE_THEM"]

class TreasuryProjectionListItemsItemResultSourceBlock(TypedDict):
    number: str
    hash: str
    timestamp: str

class TreasuryProjectionListItemsItemResultUnit(TypedDict):
    chainId: int
    genesisHash: str
    asset: str
    decimals: int

class TreasuryProjectionListItemsItemResultOpening(TypedDict):
    availableMappedAtomic: str
    declaredRestrictedAtomic: str
    scenarioBalanceAtomic: str

class TreasuryProjectionListItemsItemResultSelectedMappingsItem(TypedDict):
    ledgerEntryId: str
    ledgerResourceVersion: str
    custodyEvidenceId: str
    custodyResourceVersion: str
    ledgerState: Literal["AVAILABLE", "DEPLOYED", "LOCKED", "AT_RISK", "FEE_GENERATING"]
    ledgerAmountAtomic: str
    declaredRestrictedAtomic: str
    restrictionReason: str
    includedInOpening: bool
    disposition: Literal["AVAILABLE_DECLARED_SCENARIO", "NON_AVAILABLE_EXCLUDED"]

class TreasuryProjectionListItemsItemResultTimelineItem(TypedDict):
    day: str
    actualInflowsAtomic: Literal["0"]
    obligationsAtomic: str
    allocationsAtomic: str
    conditionalInflowsAtomic: str
    closingBaselineAtomic: str
    cumulativeConditionalAtomic: str
    closingConditionalScenarioAtomic: str

class TreasuryProjectionListItemsItemResultExcludedEventsItem(TypedDict):
    id: str
    kind: Literal["OBLIGATION", "ALLOCATION", "CONDITIONAL_INFLOW"]
    day: str
    amountAtomic: str
    reason: Literal["AFTER_HORIZON"]

class TreasuryProjectionListItemsItemResultDeclaredExpenseCoverage(TypedDict):
    declaration: Literal["DECLARED_COMPLETE", "DECLARED_PARTIAL", "UNKNOWN"]
    omittedCategories: list[str]
    note: str

class TreasuryProjectionListItemsItemResult(TypedDict):
    schemaVersion: Literal["treasury-snapshot-projection-model-v1"]
    organizationId: str
    assumptions: TreasuryProjectionListItemsItemResultAssumptions
    reconciliation: TreasuryProjectionListItemsItemResultReconciliation
    request: TreasuryProjectionListItemsItemResultRequest
    sourceBlock: TreasuryProjectionListItemsItemResultSourceBlock
    sourceCutoff: str
    unit: TreasuryProjectionListItemsItemResultUnit
    openingDay: str
    throughDay: str
    opening: TreasuryProjectionListItemsItemResultOpening
    selectedMappings: list[TreasuryProjectionListItemsItemResultSelectedMappingsItem]
    timeline: list[TreasuryProjectionListItemsItemResultTimelineItem]
    excludedEvents: list[TreasuryProjectionListItemsItemResultExcludedEventsItem]
    firstShortfallDay: Union[str, None]
    minimumBaselineAtomic: str
    closingBaselineAtomic: str
    conditionalInflowsAtomic: str
    closingConditionalScenarioAtomic: str
    declaredExpenseCoverage: TreasuryProjectionListItemsItemResultDeclaredExpenseCoverage
    provenance: Literal["DECLARED_SCENARIO"]
    verifiedExpenseCoverage: Literal["UNKNOWN"]
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]
    limitations: list[Literal["ISSUER_DECLARATIONS_ARE_NOT_VERIFIED_SPENDABILITY", "EXPENSE_COMPLETENESS_REMAINS_UNKNOWN", "SNAPSHOT_DAY_UNPAID_OUTFLOWS_ARE_INCLUDED", "DAILY_BUCKETS_DO_NOT_ESTABLISH_INTRADAY_SOLVENCY", "CONDITIONAL_INCOME_IS_NOT_SETTLED_CASH", "UNALLOCATED_CUSTODY_SURPLUS_IS_EXCLUDED", "NON_AVAILABLE_LEDGER_BALANCES_ARE_EXCLUDED", "RESTRICTIONS_ARE_DECLARED_SEPARATELY_FROM_SCHEDULES", "HISTORICAL_SOURCES_DO_NOT_ESTABLISH_CURRENT_APPLICABILITY"]]
    modelHash: str

class TreasuryProjectionListItemsItem(TypedDict):
    schemaVersion: Literal["treasury-declared-projection-v1"]
    organizationId: str
    id: str
    resourceVersion: str
    request: TreasuryProjectionListItemsItemRequest
    result: TreasuryProjectionListItemsItemResult
    sourceHash: str
    createdBy: str
    createdAt: str
    spendability: Literal["NOT_ESTABLISHED"]
    financialAuthority: Literal[False]

class TreasuryProjectionList(TypedDict):
    items: list[TreasuryProjectionListItemsItem]
    nextCursor: Union[str, None]

class MarketDiscoveryProject(TypedDict):
    id: int
    name: str
    symbol: str
    chain: str
    address: Union[str, None]
    imageUrl: Union[str, None]
    url: str

class MarketDiscoverySearch(TypedDict):
    projects: list[MarketDiscoveryProject]
    page: int
    hasMore: bool

class MarketDiscoveryPool(TypedDict):
    id: str
    venue: str
    address: str
    quote: str
    priceUsd: Union[float, None]
    liquidityUsd: Union[float, None]
    volume24hUsd: Union[float, None]
    priceChange24hPercent: Union[float, None]
    buys24h: Union[float, None]
    sells24h: Union[float, None]
    url: str

class WorkflowVaultSnapshot(TypedDict):
    id: str
    chainId: int
    capturedAt: str
    blockNumber: str
    blockHash: str
    tokenBalance: str
    quoteBalance: str
    deployedTokenBalance: str
    deployedQuoteBalance: str
    protectedQuoteReserve: str
    quoteSymbol: str
    positions: int
    paused: Union[bool, None]

class WorkflowVaultContext(TypedDict):
    vaultId: str
    name: str
    lifecycle: str
    mode: str
    projectToken: str
    quoteToken: str
    snapshot: Union[WorkflowVaultSnapshot, None]
    limitation: str

class MarketDiscoveryEvidenceMetrics(TypedDict):
    priceUsd: Union[float, None]
    liquidityUsd: Union[float, None]
    volume24hUsd: Union[float, None]
    priceChange24hPercent: Union[float, None]
    largestPoolSharePercent: Union[float, None]

class MarketDiscoveryEvidenceSourcesItem(TypedDict):
    id: str
    label: str
    url: str

class MarketDiscoveryEvidence(TypedDict):
    project: MarketDiscoveryProject
    retrievedAt: str
    pools: list[MarketDiscoveryPool]
    metrics: MarketDiscoveryEvidenceMetrics
    sources: list[MarketDiscoveryEvidenceSourcesItem]
    gaps: list[str]
    workspace: NotRequired[WorkflowVaultContext]

class MarketDiscoveryCapabilities(TypedDict):
    model: str
    configured: bool
    access: Literal["AUTHENTICATED_WORKSPACE"]
    execution: Literal["READ_ONLY"]

class WorkflowContextVaultsItem(TypedDict):
    id: str
    name: str

class WorkflowContext(TypedDict):
    vaults: list[WorkflowContextVaultsItem]
    available: bool
    persistence: bool

class WorkflowResearchRequestHistoryItem(TypedDict):
    question: str
    answer: str

class WorkflowResearchRequest(TypedDict):
    vaultId: NotRequired[str]
    projectId: int
    question: str
    history: NotRequired[list[WorkflowResearchRequestHistoryItem]]

class WorkflowResearchAnswerFindingsItem(TypedDict):
    title: str
    detail: str
    sourceIds: list[str]

class WorkflowResearchAnswerNextStepsItem(TypedDict):
    title: str
    reason: str

class WorkflowResearchAnswer(TypedDict):
    headline: str
    explanation: str
    findings: list[WorkflowResearchAnswerFindingsItem]
    nextSteps: list[WorkflowResearchAnswerNextStepsItem]
    unknowns: list[str]
    followUps: list[str]

class WorkflowResearchResult(TypedDict):
    id: str
    question: str
    evidence: MarketDiscoveryEvidence
    answer: WorkflowResearchAnswer
    completedAt: str
    execution: Literal["READ_ONLY"]

class WorkflowResearchResponse(TypedDict):
    id: str
    question: str
    evidence: MarketDiscoveryEvidence
    answer: WorkflowResearchAnswer
    completedAt: str
    execution: Literal["READ_ONLY"]
    persistence: Literal["SAVED", "SESSION"]

class CompletedWorkflowSummary(TypedDict):
    organizationId: str
    requesterId: str
    id: str
    vaultId: Union[str, None]
    projectId: int
    projectName: str
    question: str
    headline: str
    completedAt: str
    savedAt: str
    contentHash: Hash

class CompletedWorkflowRun(TypedDict):
    organizationId: str
    requesterId: str
    id: str
    vaultId: Union[str, None]
    projectId: int
    projectName: str
    question: str
    headline: str
    completedAt: str
    savedAt: str
    contentHash: Hash
    result: WorkflowResearchResult

class CompletedWorkflowPage(TypedDict):
    runs: list[CompletedWorkflowSummary]
    nextCursor: Union[str, None]

class SavedVirtualsProjectProject(TypedDict):
    id: int
    name: str
    symbol: str
    chain: str
    address: Union[str, None]
    imageUrl: Union[str, None]
    url: str

class SavedVirtualsProject(TypedDict):
    kind: Literal["VIRTUALS_DIRECTORY_PROJECT"]
    organizationId: str
    virtualsProjectId: int
    project: SavedVirtualsProjectProject
    directoryObservedAt: str
    savedAt: str
    savedBy: str
    resourceVersion: Hash

class SavedVirtualsProjectPage(TypedDict):
    projects: list[SavedVirtualsProject]
    nextCursor: Union[str, None]

class SaveVirtualsProjectRequest(TypedDict):
    virtualsProjectId: int

class SaveVirtualsProjectReceipt(TypedDict):
    project: SavedVirtualsProject
    replayed: bool

class RemoveVirtualsProjectRequest(TypedDict):
    expectedResourceVersion: Hash

class RemoveVirtualsProjectReceipt(TypedDict):
    virtualsProjectId: int
    resourceVersion: Hash
    removedAt: str
    replayed: bool

class TreasuryLedgerVersionPageItemsItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: TreasuryBucket
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class TreasuryLedgerVersionPage(TypedDict):
    items: list[TreasuryLedgerVersionPageItemsItem]
    nextCursor: Union[str, None]

class ProposalReviewDecisionEventPayloadVariant1(TypedDict):
    actorId: str
    actorRole: str
    decidedAt: str
    proposalPacketHash: Hash
    decision: Literal["APPROVE"]
    evidenceHash: str

class ProposalReviewDecisionEventPayloadVariant2(TypedDict):
    actorId: str
    actorRole: str
    decidedAt: str
    proposalPacketHash: Hash
    decision: Literal["REJECT"]
    rejectionReason: str
    evidenceHash: NotRequired[str]

class ProposalReviewDecisionEvent(TypedDict):
    organizationId: str
    eventId: str
    recordType: Literal["PROPOSAL_WORKSPACE"]
    recordId: str
    eventKind: Literal["PROPOSAL_INTERNAL_DECISION"]
    payload: Union[ProposalReviewDecisionEventPayloadVariant1, ProposalReviewDecisionEventPayloadVariant2]
    artifactHash: Hash
    createdBy: str
    actorRole: str
    reason: str
    requestId: str
    createdAt: str

class ProposalReviewCommentEventPayload(TypedDict):
    id: str
    proposalWorkspaceId: str
    authorId: str
    body: str
    mentions: list[str]
    supersedesCommentId: NotRequired[str]
    supersedesCommentArtifactHash: NotRequired[Hash]

class ProposalReviewCommentEvent(TypedDict):
    organizationId: str
    eventId: str
    recordType: Literal["PROPOSAL_WORKSPACE"]
    recordId: str
    eventKind: Literal["COMMENT_APPENDED"]
    payload: ProposalReviewCommentEventPayload
    artifactHash: Hash
    createdBy: str
    actorRole: str
    reason: str
    requestId: str
    createdAt: str

class ProposalReviewSafeSubmissionEventPayloadExecutionResult(TypedDict):
    schemaVersion: Literal["canonical-evm-execution-result-v1"]
    executionSucceeded: Literal[True]
    returnDataHash: Hash
    logsHash: Hash
    stateDeltaHash: Hash

class ProposalReviewSafeSubmissionEventPayload(TypedDict):
    schemaVersion: Literal["proposal-safe-submission-evidence-v1"]
    proposalId: str
    proposalPacketHash: Hash
    chainId: Literal[677, 968]
    safeAddress: Address
    target: Address
    value: Literal["0"]
    operation: Literal[0]
    calldata: str
    calldataHash: Hash
    decodedControllerExecution: ControllerExecutionBindingV2
    decodedControllerExecutionHash: Hash
    transactionHash: Hash
    safeTransactionHash: Hash
    finalizedBlockNumber: str
    finalizedBlockHash: Hash
    finalizedAt: str
    finalityDepth: int
    receiptStatus: Literal[1]
    executionResult: ProposalReviewSafeSubmissionEventPayloadExecutionResult
    executionResultHash: Hash
    finalityEvidenceHash: Hash
    reconciliationBlockNumber: str
    reconciliationBlockHash: Hash
    reconciledAt: str
    reconciliationStatus: Literal["MATCHED"]
    reconciliationEvidenceHash: Hash
    safeVerificationId: str
    safeVerificationEvidenceHash: Hash
    signedReleaseDigest: NotRequired[Hash]
    vaultId: str
    vaultDeploymentProvenanceHash: Hash
    vaultDeploymentBlockHash: Hash
    venueId: str
    venueResourceVersion: Hash
    venueArtifactHash: Hash
    callerSuppliedTransactionHashAccepted: Literal[False]
    executionPerformedByRoute: Literal[False]
    checkedAt: str

class ProposalReviewSafeSubmissionEvent(TypedDict):
    organizationId: str
    eventId: str
    recordType: Literal["PROPOSAL_WORKSPACE"]
    recordId: str
    eventKind: Literal["PROPOSAL_SAFE_SUBMISSION_VERIFIED"]
    payload: ProposalReviewSafeSubmissionEventPayload
    artifactHash: Hash
    createdBy: str
    actorRole: str
    reason: str
    requestId: str
    createdAt: str

class ProposalWorkspaceReviewProposal(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProposalWorkspace
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ProposalWorkspaceReviewApprovalsItem(TypedDict):
    actorId: str
    decidedAt: str
    evidenceHash: str

class ProposalWorkspaceReviewApprovalProgress(TypedDict):
    approved: int
    required: int

class ProposalWorkspaceReviewViewer(TypedDict):
    actorId: str
    role: str
    hasApproved: bool
    mayComment: bool
    mayApprove: bool
    mayReject: bool

class ProposalWorkspaceReview(TypedDict):
    schemaVersion: Literal["proposal-review-view-v1"]
    proposal: ProposalWorkspaceReviewProposal
    proposalPacketHash: Hash
    reviewEvidenceHash: Hash
    observedAt: str
    approvals: list[ProposalWorkspaceReviewApprovalsItem]
    approvalProgress: ProposalWorkspaceReviewApprovalProgress
    decisions: list[ProposalReviewDecisionEvent]
    comments: list[ProposalReviewCommentEvent]
    safeSubmissions: list[ProposalReviewSafeSubmissionEvent]
    viewer: ProposalWorkspaceReviewViewer
    executionAuthorityGranted: Literal[False]

class WorkflowRequestErrorError(TypedDict):
    message: str

class WorkflowRequestError(TypedDict):
    error: WorkflowRequestErrorError

class WorkflowRateLimitErrorError(TypedDict):
    code: Literal["RATE_LIMITED"]
    message: str
    retryable: Literal[True]
    retryAfterSeconds: int

class WorkflowRateLimitError(TypedDict):
    error: WorkflowRateLimitErrorError

class GetResearchPlanningPath(TypedDict):
    runId: str

class GetResearchPlanningResult(TypedDict):
    data: ResearchPlanningState

class GetResearchProgressPath(TypedDict):
    runId: str

class GetResearchProgressResult(TypedDict):
    data: ResearchProgress

class GetResearchTrialInputPath(TypedDict):
    runId: str
    trialKey: Literal["baseline", "alternative-1", "alternative-2", "alternative-3"]

class GetResearchTrialInputResult(TypedDict):
    data: ResearchTrialInput

class GetAgentRunResultPath(TypedDict):
    runId: str

class GetAgentRunResultResult(TypedDict):
    data: AgentRunResult

class GetAgentRunEvidencePath(TypedDict):
    runId: str
    evidenceId: str

class GetAgentRunEvidenceResult(TypedDict):
    data: CapturedHealthEvidenceView

class ApplyAgentRunCommandPath(TypedDict):
    runId: str

ApplyAgentRunCommandBody: TypeAlias = AgentControlCommand

class ApplyAgentRunCommandResult(TypedDict):
    data: AgentControlReceipt

StartHealthAgentRunBody: TypeAlias = AgentAdmissionRequest

class StartHealthAgentRunResult(TypedDict):
    data: AgentAdmissionReceipt

class ListAgentRunsQuery(TypedDict):
    limit: NotRequired[int]
    cursor: NotRequired[str]
    kind: NotRequired[Literal["HEALTH_INVESTIGATION", "PROPOSAL_REVIEW", "WHAT_IF_RESEARCH"]]
    state: NotRequired[Literal["QUEUED", "RUNNING", "WAITING_FOR_INPUT", "WAITING_FOR_CHILDREN", "COMPLETED", "PARTIAL", "ABSTAINED", "FAILED", "CANCELLED"]]
    subjectRecordType: NotRequired[Literal["VAULT", "PROPOSAL", "PROPOSAL_WORKSPACE", "ISSUER_INTENT", "SAVED_PUBLIC_PROJECT", "DECISION_PACK"]]
    subjectRecordId: NotRequired[str]

class ListAgentRunsResult(TypedDict):
    data: AgentRunList

class GetAgentRunPath(TypedDict):
    runId: str

class GetAgentRunResult(TypedDict):
    data: AgentRunDetail

class ListAgentRunEventsPath(TypedDict):
    runId: str

class ListAgentRunEventsQuery(TypedDict):
    after: NotRequired[str]
    limit: NotRequired[int]

class ListAgentRunEventsResult(TypedDict):
    data: AgentActivityPage

ResolvePublicProjectBody: TypeAlias = PublicProjectResolveRequest

class ResolvePublicProjectResult(TypedDict):
    data: PublicProjectAnalysis

InvestigatePublicProjectLiquidityBody: TypeAlias = PublicLiquidityInvestigationRequest

class InvestigatePublicProjectLiquidityResult(TypedDict):
    data: PublicLiquidityInvestigation

class ListSavedProjectsQuery(TypedDict):
    limit: NotRequired[int]
    cursor: NotRequired[str]

class ListSavedProjectsResult(TypedDict):
    data: SavedProjectList

SavePublicProjectBody: TypeAlias = PublicProjectResolveRequest

class SavePublicProjectResult(TypedDict):
    data: SavedProjectWriteReceipt

class GetSavedProjectPath(TypedDict):
    projectId: str

class GetSavedProjectResult(TypedDict):
    data: SavedPublicProject

class RefreshSavedProjectPath(TypedDict):
    projectId: str

class RefreshSavedProjectBody(TypedDict):
    pass

class RefreshSavedProjectResult(TypedDict):
    data: SavedProjectWriteReceipt

class ListSavedProjectObservationsPath(TypedDict):
    projectId: str

class ListSavedProjectObservationsQuery(TypedDict):
    limit: NotRequired[int]
    cursor: NotRequired[str]

class ListSavedProjectObservationsResult(TypedDict):
    data: SavedProjectObservationList

class GetSavedProjectObservationPath(TypedDict):
    projectId: str
    version: str

class GetSavedProjectObservationResult(TypedDict):
    data: SavedProjectObservation

class ListWorkspacePlansResult(TypedDict):
    data: WorkspacePlanCatalog

class GetPublicAcpOfferingResult(TypedDict):
    data: AcpOfferingPreview

CreateTreasuryDecisionPackBody: TypeAlias = CreateTreasuryDecisionPack

class CreateTreasuryDecisionPackResult(TypedDict):
    data: DecisionPackWriteReceipt

CreateResearchDecisionPackBody: TypeAlias = CreateResearchDecisionPack

class CreateResearchDecisionPackResult(TypedDict):
    data: DecisionPackWriteReceipt

class ListDecisionPacksQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListDecisionPacksResult(TypedDict):
    data: DecisionPackList

CreateDecisionPackBody: TypeAlias = CreateDecisionPack

class CreateDecisionPackResult(TypedDict):
    data: DecisionPackWriteReceipt

class GetDecisionPackPath(TypedDict):
    packId: str

class GetDecisionPackResult(TypedDict):
    data: DecisionPack

class ListDecisionPackVersionsPath(TypedDict):
    packId: str

class ListDecisionPackVersionsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListDecisionPackVersionsResult(TypedDict):
    data: DecisionPackHistory

class GetDecisionPackVersionPath(TypedDict):
    packId: str
    sequence: str

class GetDecisionPackVersionResult(TypedDict):
    data: DecisionPack

class ApplyDecisionPackCommandPath(TypedDict):
    packId: str

ApplyDecisionPackCommandBody: TypeAlias = DecisionPackCommand

class ApplyDecisionPackCommandResult(TypedDict):
    data: DecisionPackWriteReceipt

class ListTreasuryCustodyEvidenceQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListTreasuryCustodyEvidenceResult(TypedDict):
    data: TreasuryEvidenceList

AdmitTreasuryCustodyEvidenceBody: TypeAlias = SignedTreasuryEvidence

class AdmitTreasuryCustodyEvidenceResult(TypedDict):
    data: TreasuryEvidenceWrite

class GetTreasuryCustodyEvidencePath(TypedDict):
    evidenceId: str

class GetTreasuryCustodyEvidenceResult(TypedDict):
    data: PersistedTreasuryEvidence

IssueProjectControlChallengeBody: TypeAlias = ProjectControlIssue

class IssueProjectControlChallengeResult(TypedDict):
    data: ProjectControlChallengeWrite

class GetProjectControlChallengePath(TypedDict):
    nonce: str

class GetProjectControlChallengeResult(TypedDict):
    data: PersistedProjectControlChallenge

AcceptProjectControlProofBody: TypeAlias = ProjectControlProof

class AcceptProjectControlProofResult(TypedDict):
    data: ProjectControlAcceptance

PreviewTreasuryReconciliationBody: TypeAlias = TreasuryReconciliationPreviewRequest

class PreviewTreasuryReconciliationResult(TypedDict):
    data: TreasuryLedgerReconciliation

class ListTreasuryReconciliationsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListTreasuryReconciliationsResult(TypedDict):
    data: TreasuryReconciliationList

CreateTreasuryReconciliationBody: TypeAlias = TreasuryReconciliationPreviewRequest

class CreateTreasuryReconciliationResult(TypedDict):
    data: TreasuryReconciliationWrite

class GetTreasuryReconciliationPath(TypedDict):
    id: str

class GetTreasuryReconciliationResult(TypedDict):
    data: SavedTreasuryReconciliation

class ListTreasuryReconciliationVersionsPath(TypedDict):
    id: str

class ListTreasuryReconciliationVersionsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListTreasuryReconciliationVersionsResult(TypedDict):
    data: TreasuryReconciliationHistory

class GetTreasuryReconciliationVersionPath(TypedDict):
    id: str
    sequence: str

class GetTreasuryReconciliationVersionResult(TypedDict):
    data: SavedTreasuryReconciliation

class AcknowledgeTreasuryReconciliationPath(TypedDict):
    id: str

class AcknowledgeTreasuryReconciliationBody(TypedDict):
    confirmation: Literal["CONFIRM_LEDGER_CUSTODY_MAPPING"]

class AcknowledgeTreasuryReconciliationResult(TypedDict):
    data: TreasuryReconciliationWrite

class ListTreasuryAssumptionsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListTreasuryAssumptionsResult(TypedDict):
    data: TreasuryAssumptionsList

CreateTreasuryAssumptionsBody: TypeAlias = TreasuryAssumptionsCreate

class CreateTreasuryAssumptionsResult(TypedDict):
    data: TreasuryAssumptionsWrite

class GetTreasuryAssumptionsPath(TypedDict):
    id: str

class GetTreasuryAssumptionsResult(TypedDict):
    data: TreasuryAssumptions

class ListTreasuryAssumptionsVersionsPath(TypedDict):
    id: str

class ListTreasuryAssumptionsVersionsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListTreasuryAssumptionsVersionsResult(TypedDict):
    data: TreasuryAssumptionsHistory

class GetTreasuryAssumptionsVersionPath(TypedDict):
    id: str
    sequence: str

class GetTreasuryAssumptionsVersionResult(TypedDict):
    data: TreasuryAssumptions

class ReviseTreasuryAssumptionsPath(TypedDict):
    id: str

ReviseTreasuryAssumptionsBody: TypeAlias = TreasuryAssumptionsRevision

class ReviseTreasuryAssumptionsResult(TypedDict):
    data: TreasuryAssumptionsWrite

class ListTreasuryProjectionsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListTreasuryProjectionsResult(TypedDict):
    data: TreasuryProjectionList

CreateTreasuryProjectionBody: TypeAlias = TreasuryProjectionCreate

class CreateTreasuryProjectionResult(TypedDict):
    data: TreasuryProjectionWrite

class GetTreasuryProjectionPath(TypedDict):
    id: str

class GetTreasuryProjectionResult(TypedDict):
    data: TreasuryProjection

class SearchDiscoveredProjectsQuery(TypedDict):
    q: str
    page: NotRequired[int]

class SearchDiscoveredProjectsResult(TypedDict):
    data: MarketDiscoverySearch

class GetDiscoveredProjectMarketPath(TypedDict):
    id: int

class GetDiscoveredProjectMarketResult(TypedDict):
    data: MarketDiscoveryEvidence

class GetMarketDiscoveryCapabilitiesResult(TypedDict):
    data: MarketDiscoveryCapabilities

class GetWorkflowContextResult(TypedDict):
    data: WorkflowContext

class ListCompletedWorkflowRunsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListCompletedWorkflowRunsResult(TypedDict):
    data: CompletedWorkflowPage

class GetCompletedWorkflowRunPath(TypedDict):
    id: str

class GetCompletedWorkflowRunResult(TypedDict):
    data: CompletedWorkflowRun

RunWorkflowResearchBody: TypeAlias = WorkflowResearchRequest

class RunWorkflowResearchResult(TypedDict):
    data: WorkflowResearchResponse

class ListSavedVirtualsProjectsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListSavedVirtualsProjectsResult(TypedDict):
    data: SavedVirtualsProjectPage

SaveVirtualsProjectBody: TypeAlias = SaveVirtualsProjectRequest

class SaveVirtualsProjectResult(TypedDict):
    data: SaveVirtualsProjectReceipt

class GetSavedVirtualsProjectPath(TypedDict):
    id: int

class GetSavedVirtualsProjectResult(TypedDict):
    data: SavedVirtualsProject

class RemoveSavedVirtualsProjectPath(TypedDict):
    id: int

RemoveSavedVirtualsProjectBody: TypeAlias = RemoveVirtualsProjectRequest

class RemoveSavedVirtualsProjectResult(TypedDict):
    data: RemoveVirtualsProjectReceipt

class ListTreasuryLedgerEntryVersionsPath(TypedDict):
    id: str

class ListTreasuryLedgerEntryVersionsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListTreasuryLedgerEntryVersionsResult(TypedDict):
    data: TreasuryLedgerVersionPage

class GetProposalWorkspaceReviewPath(TypedDict):
    id: str

class GetProposalWorkspaceReviewQuery(TypedDict):
    resourceVersion: Hash

class GetProposalWorkspaceReviewResult(TypedDict):
    data: ProposalWorkspaceReview

class ListIntentsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListIntentsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: IssuerIntent
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListIntentsResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListIntentsResult(TypedDict):
    data: list[ListIntentsResultDataItem]
    meta: ListIntentsResultMeta

class CreateIntentsBody(TypedDict):
    payload: IssuerIntent
    status: NotRequired[OperatingSystemRecordStatus]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class CreateIntentsResultDataIntent(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: IssuerIntent
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateIntentsResultDataCapitalRequirement(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: CapitalRequirementStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateIntentsResultData(TypedDict):
    intent: CreateIntentsResultDataIntent
    capitalRequirement: CreateIntentsResultDataCapitalRequirement

class CreateIntentsResult(TypedDict):
    data: CreateIntentsResultData

class GetIntentsPath(TypedDict):
    id: str

class GetIntentsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: IssuerIntent
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetIntentsResult(TypedDict):
    data: GetIntentsResultData

class SupersedeIntentsPath(TypedDict):
    id: str

class SupersedeIntentsBody(TypedDict):
    payload: NotRequired[IssuerIntent]
    status: NotRequired[Literal["DRAFT", "VALIDATED", "PAUSED", "REVOKED"]]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class SupersedeIntentsResultDataIntent(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: IssuerIntent
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class SupersedeIntentsResultDataCapitalRequirement(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: CapitalRequirementStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class SupersedeIntentsResultData(TypedDict):
    intent: SupersedeIntentsResultDataIntent
    capitalRequirement: SupersedeIntentsResultDataCapitalRequirement
    validationEvidence: OperatingSystemEvent

class SupersedeIntentsResult(TypedDict):
    data: SupersedeIntentsResultData

class ListStudiesQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListStudiesResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: SimulationStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListStudiesResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListStudiesResult(TypedDict):
    data: list[ListStudiesResultDataItem]
    meta: ListStudiesResultMeta

CreateStudiesBody: TypeAlias = SimulationStudyRequest

class CreateStudiesResultDataVariant1(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: SimulationStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateStudiesResultDataVariant2Study(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: SimulationStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateStudiesResultDataVariant2(TypedDict):
    study: CreateStudiesResultDataVariant2Study
    job: OperatingSystemJob
    interactive: Literal[False]
    signedReportPending: Literal[True]

class CreateStudiesResult(TypedDict):
    data: Union[CreateStudiesResultDataVariant1, CreateStudiesResultDataVariant2]

class GetStudiesPath(TypedDict):
    id: str

class GetStudiesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: SimulationStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetStudiesResult(TypedDict):
    data: GetStudiesResultData

class ListStudySharesQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListStudySharesResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StudyShare
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListStudySharesResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListStudySharesResult(TypedDict):
    data: list[ListStudySharesResultDataItem]
    meta: ListStudySharesResultMeta

class GetStudySharesPath(TypedDict):
    id: str

class GetStudySharesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StudyShare
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetStudySharesResult(TypedDict):
    data: GetStudySharesResultData

class ListStrategiesQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListStrategiesResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyDefinitionV2
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListStrategiesResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListStrategiesResult(TypedDict):
    data: list[ListStrategiesResultDataItem]
    meta: ListStrategiesResultMeta

class CreateStrategiesBody(TypedDict):
    payload: StrategyDefinitionV2Input
    status: NotRequired[OperatingSystemRecordStatus]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class CreateStrategiesResultDataStrategy(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyDefinitionV2
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateStrategiesResultData(TypedDict):
    strategy: CreateStrategiesResultDataStrategy
    compilation: StrategyCompilation

class CreateStrategiesResult(TypedDict):
    data: CreateStrategiesResultData

class GetStrategiesPath(TypedDict):
    id: str

class GetStrategiesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyDefinitionV2
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetStrategiesResult(TypedDict):
    data: GetStrategiesResultData

class SupersedeStrategiesPath(TypedDict):
    id: str

class SupersedeStrategiesBody(TypedDict):
    payload: NotRequired[StrategyDefinitionV2Input]
    status: NotRequired[Literal["DRAFT", "VALIDATED", "PAUSED", "REVOKED"]]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class SupersedeStrategiesResultDataStrategy(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyDefinitionV2
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class SupersedeStrategiesResultData(TypedDict):
    strategy: SupersedeStrategiesResultDataStrategy
    compilation: StrategyCompilation
    compilationEvidence: OperatingSystemEvent

class SupersedeStrategiesResult(TypedDict):
    data: SupersedeStrategiesResultData

class ListProposalsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListProposalsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProposalWorkspace
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListProposalsResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListProposalsResult(TypedDict):
    data: list[ListProposalsResultDataItem]
    meta: ListProposalsResultMeta

class CreateProposalsBody(TypedDict):
    payload: ProposalWorkspaceInput
    status: NotRequired[OperatingSystemRecordStatus]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class CreateProposalsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProposalWorkspace
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateProposalsResult(TypedDict):
    data: CreateProposalsResultData

class GetProposalsPath(TypedDict):
    id: str

class GetProposalsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProposalWorkspace
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetProposalsResult(TypedDict):
    data: GetProposalsResultData

class ListLaunchPlansQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListLaunchPlansResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: LaunchPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListLaunchPlansResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListLaunchPlansResult(TypedDict):
    data: list[ListLaunchPlansResultDataItem]
    meta: ListLaunchPlansResultMeta

CreateLaunchPlansBody: TypeAlias = LaunchPlanRequest

class CreateLaunchPlansResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: LaunchPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateLaunchPlansResult(TypedDict):
    data: CreateLaunchPlansResultData

class GetLaunchPlansPath(TypedDict):
    id: str

class GetLaunchPlansResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: LaunchPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetLaunchPlansResult(TypedDict):
    data: GetLaunchPlansResultData

class ListUnlockImpactsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListUnlockImpactsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: UnlockImpact
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListUnlockImpactsResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListUnlockImpactsResult(TypedDict):
    data: list[ListUnlockImpactsResultDataItem]
    meta: ListUnlockImpactsResultMeta

CreateUnlockImpactsBody: TypeAlias = UnlockImpactRequest

class CreateUnlockImpactsResultDataDownstream(TypedDict):
    events: list[OperatingSystemEvent]
    jobs: list[OperatingSystemJob]

class CreateUnlockImpactsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: UnlockImpact
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash
    downstream: CreateUnlockImpactsResultDataDownstream

class CreateUnlockImpactsResult(TypedDict):
    data: CreateUnlockImpactsResultData

class GetUnlockImpactsPath(TypedDict):
    id: str

class GetUnlockImpactsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: UnlockImpact
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetUnlockImpactsResult(TypedDict):
    data: GetUnlockImpactsResultData

class ListScoresQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListScoresResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: MarketQualityScore
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListScoresResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListScoresResult(TypedDict):
    data: list[ListScoresResultDataItem]
    meta: ListScoresResultMeta

CreateScoresBody: TypeAlias = MarketQualityRequest

class CreateScoresResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: MarketQualityScore
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateScoresResult(TypedDict):
    data: CreateScoresResultData

class GetScoresPath(TypedDict):
    id: str

class GetScoresResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: MarketQualityScore
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetScoresResult(TypedDict):
    data: GetScoresResultData

class ListAttributionsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListAttributionsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ExecutionAttribution
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListAttributionsResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListAttributionsResult(TypedDict):
    data: list[ListAttributionsResultDataItem]
    meta: ListAttributionsResultMeta

CreateAttributionsBody: TypeAlias = ExecutionAttributionRequest

class CreateAttributionsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ExecutionAttribution
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateAttributionsResult(TypedDict):
    data: CreateAttributionsResultData

class GetAttributionsPath(TypedDict):
    id: str

class GetAttributionsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ExecutionAttribution
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetAttributionsResult(TypedDict):
    data: GetAttributionsResultData

class ListAnomaliesQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListAnomaliesResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: Anomaly
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListAnomaliesResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListAnomaliesResult(TypedDict):
    data: list[ListAnomaliesResultDataItem]
    meta: ListAnomaliesResultMeta

CreateAnomaliesBody: TypeAlias = AnomalyDetectionRequest

class CreateAnomaliesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: Anomaly
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateAnomaliesResult(TypedDict):
    data: CreateAnomaliesResultData

class GetAnomaliesPath(TypedDict):
    id: str

class GetAnomaliesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: Anomaly
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetAnomaliesResult(TypedDict):
    data: GetAnomaliesResultData

class ListTreasuryEntriesQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListTreasuryEntriesResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: TreasuryBucket
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListTreasuryEntriesResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListTreasuryEntriesResult(TypedDict):
    data: list[ListTreasuryEntriesResultDataItem]
    meta: ListTreasuryEntriesResultMeta

class CreateTreasuryEntriesBody(TypedDict):
    payload: TreasuryBucket
    status: NotRequired[OperatingSystemRecordStatus]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class CreateTreasuryEntriesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: TreasuryBucket
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateTreasuryEntriesResult(TypedDict):
    data: CreateTreasuryEntriesResultData

class GetTreasuryEntriesPath(TypedDict):
    id: str

class GetTreasuryEntriesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: TreasuryBucket
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetTreasuryEntriesResult(TypedDict):
    data: GetTreasuryEntriesResultData

class ListCapitalRequirementsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListCapitalRequirementsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: CapitalRequirementStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListCapitalRequirementsResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListCapitalRequirementsResult(TypedDict):
    data: list[ListCapitalRequirementsResultDataItem]
    meta: ListCapitalRequirementsResultMeta

CreateCapitalRequirementsBody: TypeAlias = CapitalRequirementRequest

class CreateCapitalRequirementsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: CapitalRequirementStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateCapitalRequirementsResult(TypedDict):
    data: CreateCapitalRequirementsResultData

class GetCapitalRequirementsPath(TypedDict):
    id: str

class GetCapitalRequirementsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: CapitalRequirementStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetCapitalRequirementsResult(TypedDict):
    data: GetCapitalRequirementsResultData

class ListTreasuryStressTestsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListTreasuryStressTestsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: TreasuryStressStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListTreasuryStressTestsResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListTreasuryStressTestsResult(TypedDict):
    data: list[ListTreasuryStressTestsResultDataItem]
    meta: ListTreasuryStressTestsResultMeta

CreateTreasuryStressTestsBody: TypeAlias = TreasuryStressRequest

class CreateTreasuryStressTestsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: TreasuryStressStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateTreasuryStressTestsResult(TypedDict):
    data: CreateTreasuryStressTestsResultData

class GetTreasuryStressTestsPath(TypedDict):
    id: str

class GetTreasuryStressTestsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: TreasuryStressStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetTreasuryStressTestsResult(TypedDict):
    data: GetTreasuryStressTestsResultData

class ListVenuesQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListVenuesResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: VenueProfile
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListVenuesResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListVenuesResult(TypedDict):
    data: list[ListVenuesResultDataItem]
    meta: ListVenuesResultMeta

class CreateVenuesBody(TypedDict):
    payload: VenueProfile
    status: NotRequired[OperatingSystemRecordStatus]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class CreateVenuesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: VenueProfile
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateVenuesResult(TypedDict):
    data: CreateVenuesResultData

class GetVenuesPath(TypedDict):
    id: str

class GetVenuesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: VenueProfile
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetVenuesResult(TypedDict):
    data: GetVenuesResultData

class SupersedeVenuesPath(TypedDict):
    id: str

class SupersedeVenuesBody(TypedDict):
    payload: NotRequired[VenueProfile]
    status: NotRequired[Literal["DRAFT", "VALIDATED", "PAUSED", "REVOKED"]]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class SupersedeVenuesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: VenueProfile
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class SupersedeVenuesResult(TypedDict):
    data: SupersedeVenuesResultData

class ListVenueObservationsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListVenueObservationsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: VenueObservation
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListVenueObservationsResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListVenueObservationsResult(TypedDict):
    data: list[ListVenueObservationsResultDataItem]
    meta: ListVenueObservationsResultMeta

class GetVenueObservationsPath(TypedDict):
    id: str

class GetVenueObservationsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: VenueObservation
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetVenueObservationsResult(TypedDict):
    data: GetVenueObservationsResultData

class ListAllocationPlansQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListAllocationPlansResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: AllocationPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListAllocationPlansResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListAllocationPlansResult(TypedDict):
    data: list[ListAllocationPlansResultDataItem]
    meta: ListAllocationPlansResultMeta

CreateAllocationPlansBody: TypeAlias = AllocationRequest

class CreateAllocationPlansResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: AllocationPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateAllocationPlansResult(TypedDict):
    data: CreateAllocationPlansResultData

class GetAllocationPlansPath(TypedDict):
    id: str

class GetAllocationPlansResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: AllocationPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetAllocationPlansResult(TypedDict):
    data: GetAllocationPlansResultData

class ListMigrationPlansQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListMigrationPlansResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: MigrationPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListMigrationPlansResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListMigrationPlansResult(TypedDict):
    data: list[ListMigrationPlansResultDataItem]
    meta: ListMigrationPlansResultMeta

CreateMigrationPlansBody: TypeAlias = MigrationRequest

class CreateMigrationPlansResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: MigrationPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateMigrationPlansResult(TypedDict):
    data: CreateMigrationPlansResultData

class GetMigrationPlansPath(TypedDict):
    id: str

class GetMigrationPlansResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: MigrationPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetMigrationPlansResult(TypedDict):
    data: GetMigrationPlansResultData

class ListAutonomyPoliciesQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListAutonomyPoliciesResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: AutonomyPolicy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListAutonomyPoliciesResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListAutonomyPoliciesResult(TypedDict):
    data: list[ListAutonomyPoliciesResultDataItem]
    meta: ListAutonomyPoliciesResultMeta

class CreateAutonomyPoliciesBody(TypedDict):
    payload: AutonomyPolicyInput
    status: NotRequired[OperatingSystemRecordStatus]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class CreateAutonomyPoliciesResultDataVariant1(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: AutonomyPolicy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateAutonomyPoliciesResultDataVariant2Policy(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: AutonomyPolicy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateAutonomyPoliciesResultDataVariant2(TypedDict):
    policy: CreateAutonomyPoliciesResultDataVariant2Policy
    safeAuthorityEvidence: OperatingSystemEvent

class CreateAutonomyPoliciesResult(TypedDict):
    data: Union[CreateAutonomyPoliciesResultDataVariant1, CreateAutonomyPoliciesResultDataVariant2]

class GetAutonomyPoliciesPath(TypedDict):
    id: str

class GetAutonomyPoliciesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: AutonomyPolicy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetAutonomyPoliciesResult(TypedDict):
    data: GetAutonomyPoliciesResultData

class SupersedeAutonomyPoliciesPath(TypedDict):
    id: str

class SupersedeAutonomyPoliciesBody(TypedDict):
    payload: NotRequired[AutonomyPolicy]
    status: NotRequired[Literal["ACTIVE", "PAUSED", "REVOKED"]]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class SupersedeAutonomyPoliciesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: AutonomyPolicy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class SupersedeAutonomyPoliciesResult(TypedDict):
    data: SupersedeAutonomyPoliciesResultData

class ListPolicyIntentDraftsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListPolicyIntentDraftsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PolicyIntentDraft
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListPolicyIntentDraftsResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListPolicyIntentDraftsResult(TypedDict):
    data: list[ListPolicyIntentDraftsResultDataItem]
    meta: ListPolicyIntentDraftsResultMeta

CreatePolicyIntentDraftsBody: TypeAlias = PolicyExtractRequest

class CreatePolicyIntentDraftsResult(TypedDict):
    data: PolicyDraftResult

class GetPolicyIntentDraftsPath(TypedDict):
    id: str

class GetPolicyIntentDraftsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PolicyIntentDraft
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetPolicyIntentDraftsResult(TypedDict):
    data: GetPolicyIntentDraftsResultData

class ListQuoteSetsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListQuoteSetsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProtectedExecutionQuoteSet
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListQuoteSetsResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListQuoteSetsResult(TypedDict):
    data: list[ListQuoteSetsResultDataItem]
    meta: ListQuoteSetsResultMeta

class AdmitProtectedExecutionQuoteSetBody(TypedDict):
    quoteRequestId: str
    quotes: list[ProtectedExecutionQuote]
    unavailableReasons: list[str]
    reason: str

class AdmitProtectedExecutionQuoteSetResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProtectedExecutionQuoteSet
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class AdmitProtectedExecutionQuoteSetResult(TypedDict):
    data: AdmitProtectedExecutionQuoteSetResultData

class GetQuoteSetsPath(TypedDict):
    id: str

class GetQuoteSetsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProtectedExecutionQuoteSet
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetQuoteSetsResult(TypedDict):
    data: GetQuoteSetsResultData

class ListProtectedExecutionPlansQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListProtectedExecutionPlansResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProtectedExecutionPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListProtectedExecutionPlansResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListProtectedExecutionPlansResult(TypedDict):
    data: list[ListProtectedExecutionPlansResultDataItem]
    meta: ListProtectedExecutionPlansResultMeta

class PrepareProtectedExecutionPlanBody(TypedDict):
    quoteSetId: str
    childLegCount: int
    reason: str

class PrepareProtectedExecutionPlanResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProtectedExecutionPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash
    stateHash: Hash
    publicMempoolFallbackDerivedFromPolicy: Literal[True]
    executionBroadcast: Literal[False]

class PrepareProtectedExecutionPlanResult(TypedDict):
    data: PrepareProtectedExecutionPlanResultData

class GetProtectedExecutionPlansPath(TypedDict):
    id: str

class GetProtectedExecutionPlansResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProtectedExecutionPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetProtectedExecutionPlansResult(TypedDict):
    data: GetProtectedExecutionPlansResultData

class ListDeveloperCredentialsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListDeveloperCredentialsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: DeveloperCredential
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListDeveloperCredentialsResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListDeveloperCredentialsResult(TypedDict):
    data: list[ListDeveloperCredentialsResultDataItem]
    meta: ListDeveloperCredentialsResultMeta

CreateDeveloperCredentialsBody: TypeAlias = DeveloperCredentialRequest

class CreateDeveloperCredentialsResultDataCredential(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: DeveloperCredential
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateDeveloperCredentialsResultData(TypedDict):
    credential: CreateDeveloperCredentialsResultDataCredential
    secret: str
    secretReturnedOnce: Literal[True]

class CreateDeveloperCredentialsResult(TypedDict):
    data: CreateDeveloperCredentialsResultData

class GetDeveloperCredentialsPath(TypedDict):
    id: str

class GetDeveloperCredentialsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: DeveloperCredential
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetDeveloperCredentialsResult(TypedDict):
    data: GetDeveloperCredentialsResultData

class SupersedeDeveloperCredentialsPath(TypedDict):
    id: str

class SupersedeDeveloperCredentialsBody(TypedDict):
    status: NotRequired[Literal["REVOKED"]]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class SupersedeDeveloperCredentialsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: DeveloperCredential
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class SupersedeDeveloperCredentialsResult(TypedDict):
    data: SupersedeDeveloperCredentialsResultData

class ListWebhooksQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListWebhooksResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: WebhookSubscription
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListWebhooksResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListWebhooksResult(TypedDict):
    data: list[ListWebhooksResultDataItem]
    meta: ListWebhooksResultMeta

CreateWebhooksBody: TypeAlias = WebhookRequest

class CreateWebhooksResultDataSubscription(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: WebhookSubscription
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateWebhooksResultData(TypedDict):
    subscription: CreateWebhooksResultDataSubscription
    signingSecret: str
    signatureInput: Literal["timestamp.deliveryId.body"]
    secretReturnedOnce: Literal[True]

class CreateWebhooksResult(TypedDict):
    data: CreateWebhooksResultData

class GetWebhooksPath(TypedDict):
    id: str

class GetWebhooksResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: WebhookSubscription
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetWebhooksResult(TypedDict):
    data: GetWebhooksResultData

class SupersedeWebhooksPath(TypedDict):
    id: str

class SupersedeWebhooksBody(TypedDict):
    status: NotRequired[Literal["PAUSED", "REVOKED"]]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class SupersedeWebhooksResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: WebhookSubscription
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class SupersedeWebhooksResult(TypedDict):
    data: SupersedeWebhooksResultData

class ListStrategyPackagesQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListStrategyPackagesResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyPackage
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListStrategyPackagesResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListStrategyPackagesResult(TypedDict):
    data: list[ListStrategyPackagesResultDataItem]
    meta: ListStrategyPackagesResultMeta

class CreateStrategyPackageCandidateBody(TypedDict):
    payload: StrategyPackageCandidate
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class CreateStrategyPackageCandidateResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyPackage
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateStrategyPackageCandidateResult(TypedDict):
    data: CreateStrategyPackageCandidateResultData

class GetStrategyPackagesPath(TypedDict):
    id: str

class GetStrategyPackagesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyPackage
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetStrategyPackagesResult(TypedDict):
    data: GetStrategyPackagesResultData

class ListPartnersQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListPartnersResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PartnerTenant
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListPartnersResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListPartnersResult(TypedDict):
    data: list[ListPartnersResultDataItem]
    meta: ListPartnersResultMeta

class CreateVerifiedPartnerTenantBody(TypedDict):
    payload: PartnerTenantCreate
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class CreateVerifiedPartnerTenantResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PartnerTenant
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateVerifiedPartnerTenantResult(TypedDict):
    data: CreateVerifiedPartnerTenantResultData

class GetPartnersPath(TypedDict):
    id: str

class GetPartnersResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PartnerTenant
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetPartnersResult(TypedDict):
    data: GetPartnersResultData

class UpdatePartnerConfigurationPath(TypedDict):
    id: str

class UpdatePartnerConfigurationBody(TypedDict):
    payload: PartnerTenantCreate
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class UpdatePartnerConfigurationResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PartnerTenant
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class UpdatePartnerConfigurationResult(TypedDict):
    data: UpdatePartnerConfigurationResultData

class ListMarketMakerMandatesQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListMarketMakerMandatesResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: MarketMakerMandate
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListMarketMakerMandatesResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListMarketMakerMandatesResult(TypedDict):
    data: list[ListMarketMakerMandatesResultDataItem]
    meta: ListMarketMakerMandatesResultMeta

class CreateMarketMakerMandateBody(TypedDict):
    payload: MarketMakerMandate
    status: NotRequired[OperatingSystemRecordStatus]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class CreateMarketMakerMandateResultDataMandate(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: MarketMakerMandate
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateMarketMakerMandateResultData(TypedDict):
    mandate: CreateMarketMakerMandateResultDataMandate
    oversight: MarketMakerOversight

class CreateMarketMakerMandateResult(TypedDict):
    data: CreateMarketMakerMandateResultData

class GetMarketMakerMandatesPath(TypedDict):
    id: str

class GetMarketMakerMandatesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: MarketMakerMandate
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetMarketMakerMandatesResult(TypedDict):
    data: GetMarketMakerMandatesResultData

class SupersedeMarketMakerMandatesPath(TypedDict):
    id: str

class SupersedeMarketMakerMandatesBody(TypedDict):
    status: NotRequired[Literal["PAUSED", "REVOKED"]]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class SupersedeMarketMakerMandatesResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: MarketMakerMandate
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class SupersedeMarketMakerMandatesResult(TypedDict):
    data: SupersedeMarketMakerMandatesResultData

class ListIncentiveProgramsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListIncentiveProgramsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: IncentiveProgram
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListIncentiveProgramsResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListIncentiveProgramsResult(TypedDict):
    data: list[ListIncentiveProgramsResultDataItem]
    meta: ListIncentiveProgramsResultMeta

class OptimizeIncentiveProgramBody(TypedDict):
    payload: IncentiveProgram
    status: NotRequired[OperatingSystemRecordStatus]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class OptimizeIncentiveProgramResult(TypedDict):
    data: IncentiveOptimizationResult

class GetIncentiveProgramsPath(TypedDict):
    id: str

class GetIncentiveProgramsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: IncentiveProgram
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetIncentiveProgramsResult(TypedDict):
    data: GetIncentiveProgramsResultData

class SupersedeIncentiveProgramsPath(TypedDict):
    id: str

class SupersedeIncentiveProgramsBody(TypedDict):
    status: NotRequired[Literal["REVOKED"]]
    evidenceHashes: NotRequired[list[Hash]]
    reason: str

class SupersedeIncentiveProgramsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: IncentiveProgram
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class SupersedeIncentiveProgramsResult(TypedDict):
    data: SupersedeIncentiveProgramsResultData

class ListPassportsQuery(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListPassportsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: LiquidityPassport
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListPassportsResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListPassportsResult(TypedDict):
    data: list[ListPassportsResultDataItem]
    meta: ListPassportsResultMeta

class PublishLiquidityPassportBodyPayloadReportBrandSourceBinding(TypedDict):
    partnerOrganizationId: str
    partnerConfigurationResourceVersion: Hash
    partnerConfigurationArtifactHash: Hash
    consentId: str
    consentResourceVersion: Hash
    consentArtifactHash: Hash

class PublishLiquidityPassportBodyPayloadReportBrand(TypedDict):
    partnerId: str
    name: str
    accentColor: str
    logoContentHash: NotRequired[Hash]
    sourceBinding: PublishLiquidityPassportBodyPayloadReportBrandSourceBinding

class PublishLiquidityPassportBodyPayloadUsableDepthByTradeSizeItem(TypedDict):
    tradeSizeQuote: AtomicAmount
    buySlippagePips: Pips
    sellSlippagePips: Pips

class PublishLiquidityPassportBodyPayloadPolicyLimits(TypedDict):
    level: Literal[0, 1, 2, 3, 4]
    maximumAmountPerTransaction: AtomicAmount
    maximumDailyTurnover: AtomicAmount
    maximumSlippagePips: Pips
    approvedContracts: list[Address]
    approvedAssets: list[Address]
    approvedAdapterIds: list[str]
    minimumSecondsBetweenActions: int
    minimumPriceX18: NotRequired[AtomicAmount]
    maximumPriceX18: NotRequired[AtomicAmount]
    oracleMaximumAgeSeconds: int
    expiresAt: str
    controlEpoch: AtomicAmount
    publicMempoolFallbackAllowed: bool

class PublishLiquidityPassportBodyPayloadIncidentDetailsAnomaliesItem(TypedDict):
    detectorVersion: Literal["robust-mad-v1"]
    kind: Literal["LIQUIDITY_DISAPPEARANCE", "ONE_SIDED_FLOW", "INACTIVE_RANGE", "STABLECOIN_DEPEG", "ORACLE_DISAGREEMENT", "INVENTORY_ACCUMULATION", "EXCESSIVE_TURNOVER", "MANIPULATION_INDICATOR", "SIMULATED_REALIZED_DIVERGENCE"]
    severity: Literal["INFO", "WARNING", "CRITICAL"]
    artifactHash: Hash

class PublishLiquidityPassportBodyPayloadIncidentDetails(TypedDict):
    v1IncidentEvidenceHashes: list[Hash]
    anomalies: list[PublishLiquidityPassportBodyPayloadIncidentDetailsAnomaliesItem]

class PublishLiquidityPassportBodyPayloadDisclosure(TypedDict):
    showTreasuryOwnership: bool
    showExternalManagerNames: bool
    showIncidentDetails: bool
    showPolicyLimits: bool

class PublishLiquidityPassportBodyPayloadResultsRegistryReceipt(TypedDict):
    receiptVersion: Literal["liquidity-passport-results-registry-receipt-v1"]
    providerId: str
    providerResourceVersion: Hash
    providerAttestationHash: Hash
    passportSubjectHash: Hash
    commitmentHash: Hash
    issuedAt: str
    signature: str

class PublishLiquidityPassportBodyPayload(TypedDict):
    passportVersion: Literal["liquidity-passport-v1"]
    artifactRendererVersion: Literal["liquidity-passport-artifacts-v1", "liquidity-passport-artifacts-v2"]
    signatureAlgorithm: Literal["Ed25519"]
    signerProviderId: str
    signerKeyResourceVersion: Hash
    slug: str
    vaultId: str
    issuerName: str
    reportBrand: NotRequired[PublishLiquidityPassportBodyPayloadReportBrand]
    generatedAt: str
    validUntil: str
    usableDepthByTradeSize: list[PublishLiquidityPassportBodyPayloadUsableDepthByTradeSizeItem]
    historicalReliabilityPips: Pips
    policyCompliancePips: Union[Pips, None]
    policyLimits: NotRequired[PublishLiquidityPassportBodyPayloadPolicyLimits]
    reconciledPositionCount: int
    majorIncidentCount: int
    treasuryOwnedLiquidityQuote: NotRequired[AtomicAmount]
    rentedLiquidityQuote: NotRequired[AtomicAmount]
    incidentDetails: NotRequired[PublishLiquidityPassportBodyPayloadIncidentDetails]
    externalManagerExposureQuote: NotRequired[AtomicAmount]
    externalManagerNames: NotRequired[list[str]]
    dataFreshnessSeconds: int
    disclosure: PublishLiquidityPassportBodyPayloadDisclosure
    reportHashes: list[Hash]
    sourceBindings: LiquidityPassportSourceBindings
    resultsRegistryProviderId: NotRequired[str]
    resultsRegistryProviderResourceVersion: NotRequired[Hash]
    resultsRegistryProviderAttestationHash: NotRequired[Hash]
    resultsRegistryCommitmentHash: NotRequired[Hash]
    resultsRegistryReceipt: NotRequired[PublishLiquidityPassportBodyPayloadResultsRegistryReceipt]
    supersedesPassportHash: NotRequired[Hash]
    contentHash: Hash
    signature: str
    marketQualityScoreId: str

class PublishLiquidityPassportBody(TypedDict):
    payload: PublishLiquidityPassportBodyPayload
    reason: str

class PublishLiquidityPassportResultDataPassport(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: LiquidityPassport
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class PublishLiquidityPassportResultData(TypedDict):
    passport: PublishLiquidityPassportResultDataPassport
    reportJob: OperatingSystemJob
    signedFormatsReady: list[Literal["JSON", "HTML", "PDF", "CSV"]]
    artifactState: Literal["PENDING_IMMUTABLE_OBJECT_REGISTRATION"]
    executionAuthorityGranted: Literal[False]

class PublishLiquidityPassportResult(TypedDict):
    data: PublishLiquidityPassportResultData

class GetPassportsPath(TypedDict):
    id: str

class GetPassportsResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: LiquidityPassport
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetPassportsResult(TypedDict):
    data: GetPassportsResultData

GetOperatingSystemOpenApiResult: TypeAlias = OpenApiDocument

class GetOperatingSystemStatusResult(TypedDict):
    data: OperatingSystemStatus

class IssueOperatingSystemOAuthTokenBody(TypedDict):
    grant_type: Literal["client_credentials"]
    scope: NotRequired[str]

IssueOperatingSystemOAuthTokenResult: TypeAlias = OAuthTokenResponse

class ActivateMarketQualityScorePath(TypedDict):
    id: str

ActivateMarketQualityScoreBody: TypeAlias = MarketQualityScoreActivationRequest

class ActivateMarketQualityScoreResultDataScore(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: MarketQualityScore
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ActivateMarketQualityScoreResultData(TypedDict):
    score: ActivateMarketQualityScoreResultDataScore
    review: OperatingSystemEvent
    executionAuthorityGranted: Literal[False]

class ActivateMarketQualityScoreResult(TypedDict):
    data: ActivateMarketQualityScoreResultData

class CreateProtectedExecutionQuoteRequestBody(TypedDict):
    vaultId: str
    chainId: int
    assetIn: Address
    assetOut: Address
    settlementContract: Address
    settlementAdapterId: str
    amountIn: PositiveAtomicAmount
    maximumSlippagePips: Pips
    expiresAt: str
    providerIds: list[str]
    reason: str

class CreateProtectedExecutionQuoteRequestResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProtectedExecutionQuoteRequest
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash
    publicMempoolFallbackDerivedFromPolicy: Literal[True]
    executable: Literal[False]

class CreateProtectedExecutionQuoteRequestResult(TypedDict):
    data: CreateProtectedExecutionQuoteRequestResultData

class AdmitProtectedExecutionQuotesForRequestPath(TypedDict):
    id: str

class AdmitProtectedExecutionQuotesForRequestBody(TypedDict):
    quoteRequestId: str
    quotes: list[ProtectedExecutionQuote]
    unavailableReasons: list[str]
    reason: str

class AdmitProtectedExecutionQuotesForRequestResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProtectedExecutionQuoteSet
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class AdmitProtectedExecutionQuotesForRequestResult(TypedDict):
    data: AdmitProtectedExecutionQuotesForRequestResultData

class GetProtectedExecutionPlanStatePath(TypedDict):
    id: str

class GetProtectedExecutionPlanStateResultData(TypedDict):
    plan: ProtectedExecutionPlan
    stateHash: Hash

class GetProtectedExecutionPlanStateResult(TypedDict):
    data: GetProtectedExecutionPlanStateResultData

class AppendProtectedExecutionLegTransitionPath(TypedDict):
    id: str

class AppendProtectedExecutionLegTransitionBody(TypedDict):
    childLegId: str
    toStatus: Literal["SUBMITTED", "FINALIZED_RECONCILED", "PAUSED", "FAILED"]
    previousStateHash: Hash
    reason: str

class AppendProtectedExecutionLegTransitionResultDataRecord(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: ProtectedExecutionPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class AppendProtectedExecutionLegTransitionResultData(TypedDict):
    record: AppendProtectedExecutionLegTransitionResultDataRecord
    transition: OperatingSystemEvent
    stateHash: Hash
    inputConserved: bool
    executionBroadcast: Literal[False]

class AppendProtectedExecutionLegTransitionResult(TypedDict):
    data: AppendProtectedExecutionLegTransitionResultData

class RefreshTreasuryLedgerEntryPath(TypedDict):
    id: str

RefreshTreasuryLedgerEntryBody: TypeAlias = TreasuryLedgerRefreshRequest

class RefreshTreasuryLedgerEntryResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: TreasuryBucket
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class RefreshTreasuryLedgerEntryResult(TypedDict):
    data: RefreshTreasuryLedgerEntryResultData

class RetireTreasuryLedgerEntryPath(TypedDict):
    id: str

RetireTreasuryLedgerEntryBody: TypeAlias = TreasuryLedgerRetirementRequest

class RetireTreasuryLedgerEntryResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: TreasuryBucket
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class RetireTreasuryLedgerEntryResult(TypedDict):
    data: RetireTreasuryLedgerEntryResultData

class GetOperatingSystemWorkspaceResult(TypedDict):
    data: OperatingSystemWorkspace

class ListQualifiedVaultsV2Query(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListQualifiedVaultsV2ResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListQualifiedVaultsV2Result(TypedDict):
    data: list[QualifiedVaultV2]
    meta: ListQualifiedVaultsV2ResultMeta

class GetQualifiedVaultV2Path(TypedDict):
    id: str

class GetQualifiedVaultV2Result(TypedDict):
    data: QualifiedVaultV2

class ListExecutionReceiptsV2Query(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListExecutionReceiptsV2ResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListExecutionReceiptsV2Result(TypedDict):
    data: list[ExecutionReceiptV2]
    meta: ListExecutionReceiptsV2ResultMeta

class GetExecutionReceiptV2Path(TypedDict):
    id: str

class GetExecutionReceiptV2Result(TypedDict):
    data: ExecutionReceiptV2

class ListAlertsV2Query(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListAlertsV2ResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: Anomaly
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListAlertsV2ResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListAlertsV2Result(TypedDict):
    data: list[ListAlertsV2ResultDataItem]
    meta: ListAlertsV2ResultMeta

class ListProofV2Query(TypedDict):
    cursor: NotRequired[str]
    limit: NotRequired[int]

class ListProofV2ResultMeta(TypedDict):
    count: int
    hasMore: bool
    nextCursor: NotRequired[str]

class ListProofV2Result(TypedDict):
    data: list[ProofResource]
    meta: ListProofV2ResultMeta

class ListOperatingSystemProvidersResult(TypedDict):
    data: list[OperatingSystemProvider]

PutOperatingSystemProviderBody: TypeAlias = ProviderRegistrationRequest

class PutOperatingSystemProviderResult(TypedDict):
    data: OperatingSystemProvider

class ListOperatingSystemArtifactsQuery(TypedDict):
    recordType: NotRequired[str]
    recordId: NotRequired[str]

class ListOperatingSystemArtifactsResult(TypedDict):
    data: list[OperatingSystemArtifact]

class GetTreasurySummaryResult(TypedDict):
    data: TreasurySummary

class GetUnifiedLiquidityMapResult(TypedDict):
    data: UnifiedLiquidityMap

RunNonCustodialSandboxStudyBody: TypeAlias = SandboxSimulationStudyRequest

class RunNonCustodialSandboxStudyResultDataStudy(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: SimulationStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class RunNonCustodialSandboxStudyResultData(TypedDict):
    study: RunNonCustodialSandboxStudyResultDataStudy
    sandbox: Literal[True]
    custodyAuthorityGranted: Literal[False]
    signingAuthorityGranted: Literal[False]
    executionAuthorityGranted: Literal[False]
    networkCodeExecuted: Literal[False]

class RunNonCustodialSandboxStudyResult(TypedDict):
    data: RunNonCustodialSandboxStudyResultData

class CreateStudyShareLinkPath(TypedDict):
    id: str

CreateStudyShareLinkBody: TypeAlias = StudyShareRequest

class CreateStudyShareLinkResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StudyShare
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class CreateStudyShareLinkResult(TypedDict):
    data: CreateStudyShareLinkResultData

class RevokeStudyShareLinkPath(TypedDict):
    id: str

class RevokeStudyShareLinkBody(TypedDict):
    reason: str

class RevokeStudyShareLinkResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StudyShare
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class RevokeStudyShareLinkResult(TypedDict):
    data: RevokeStudyShareLinkResultData

class RevokeLiquidityPassportPath(TypedDict):
    id: str

class RevokeLiquidityPassportBody(TypedDict):
    reason: str

class RevokeLiquidityPassportResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: LiquidityPassport
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class RevokeLiquidityPassportResult(TypedDict):
    data: RevokeLiquidityPassportResultData

class CreateSignedStudyReportPath(TypedDict):
    id: str

CreateSignedStudyReportBody: TypeAlias = SignedStudyReportRequest

class CreateSignedStudyReportResultDataSource(TypedDict):
    id: str
    version: int
    artifactHash: Hash

class CreateSignedStudyReportResultData(TypedDict):
    job: OperatingSystemJob
    source: CreateSignedStudyReportResultDataSource

class CreateSignedStudyReportResult(TypedDict):
    data: CreateSignedStudyReportResultData

class ListStudyReportJobsPath(TypedDict):
    id: str

class ListStudyReportJobsResult(TypedDict):
    data: list[OperatingSystemJob]

class WrapLegacyStrategyDefinitionBody(TypedDict):
    simulationId: str
    reason: str

class WrapLegacyStrategyDefinitionResultDataStrategy(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyDefinitionV2
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class WrapLegacyStrategyDefinitionResultData(TypedDict):
    strategy: WrapLegacyStrategyDefinitionResultDataStrategy
    compilation: StrategyCompilation
    sourceArtifactHash: Hash
    proposalAuthorityGranted: Literal[False]

class WrapLegacyStrategyDefinitionResult(TypedDict):
    data: WrapLegacyStrategyDefinitionResultData

class AdmitStrategyProposalPath(TypedDict):
    id: str

AdmitStrategyProposalBody: TypeAlias = StrategyProposalAdmissionRequest

class AdmitStrategyProposalResultData(TypedDict):
    admission: OperatingSystemEvent
    validation: StrategyProposalAdmission
    proposalAuthorityGranted: Literal[False]

class AdmitStrategyProposalResult(TypedDict):
    data: AdmitStrategyProposalResultData

class GetStrategyEvidencePath(TypedDict):
    id: str

class GetStrategyEvidenceQuery(TypedDict):
    resourceVersion: str

class GetStrategyEvidenceResultDataStrategy(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyDefinitionV2
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetStrategyEvidenceResultDataAdmissionsItemStudyVariant1(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: SimulationStudy
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetStrategyEvidenceResultDataAdmissionsItem(TypedDict):
    event: OperatingSystemEvent
    study: Union[GetStrategyEvidenceResultDataAdmissionsItemStudyVariant1, None]

class GetStrategyEvidenceResultData(TypedDict):
    schemaVersion: Literal["strategy-evidence-view-v1"]
    strategy: GetStrategyEvidenceResultDataStrategy
    admissions: list[GetStrategyEvidenceResultDataAdmissionsItem]
    executionAuthorityGranted: Literal[False]

class GetStrategyEvidenceResult(TypedDict):
    data: GetStrategyEvidenceResultData

class GetIncentiveEvidencePath(TypedDict):
    id: str

class GetIncentiveEvidenceQuery(TypedDict):
    resourceVersion: str

class GetIncentiveEvidenceResultDataProgram(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: IncentiveProgram
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetIncentiveEvidenceResultData(TypedDict):
    schemaVersion: Literal["incentive-evidence-view-v1"]
    program: GetIncentiveEvidenceResultDataProgram
    events: list[OperatingSystemEvent]
    unboundEventCount: int
    executionPerformed: Literal[False]
    executionAuthorityGranted: Literal[False]

class GetIncentiveEvidenceResult(TypedDict):
    data: GetIncentiveEvidenceResultData

class ApproveStrategyPackagePath(TypedDict):
    id: str

ApproveStrategyPackageBody: TypeAlias = StrategyPackageApprovalRequest

class ApproveStrategyPackageResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyPackage
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ApproveStrategyPackageResult(TypedDict):
    data: ApproveStrategyPackageResultData

class SeedStrategyFromApprovedPackagePath(TypedDict):
    id: str

SeedStrategyFromApprovedPackageBody: TypeAlias = StrategyPackageSeedRequest

class SeedStrategyFromApprovedPackageResultDataStrategy(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyDefinitionV2
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class SeedStrategyFromApprovedPackageResultData(TypedDict):
    strategy: SeedStrategyFromApprovedPackageResultDataStrategy
    sourcePackageId: str
    sourcePackageVersion: int
    sourcePackageResourceVersion: Hash
    sourcePackageArtifactHash: Hash
    safetyEnvelopeHash: Hash
    executionAuthorityGranted: Literal[False]
    standardProposalSimulationApprovalSafeFlowRequired: Literal[True]

class SeedStrategyFromApprovedPackageResult(TypedDict):
    data: SeedStrategyFromApprovedPackageResultData

class RevokeStrategyPackagePath(TypedDict):
    id: str

class RevokeStrategyPackageBody(TypedDict):
    reason: str

class RevokeStrategyPackageResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: StrategyPackage
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class RevokeStrategyPackageResult(TypedDict):
    data: RevokeStrategyPackageResultData

class ListProposalCommentsPath(TypedDict):
    id: str

class ListProposalCommentsResult(TypedDict):
    data: list[OperatingSystemEvent]

class AppendProposalCommentPath(TypedDict):
    id: str

AppendProposalCommentBody: TypeAlias = ProposalCommentRequest

class AppendProposalCommentResult(TypedDict):
    data: OperatingSystemEvent

class DecideProposalPath(TypedDict):
    id: str

DecideProposalBody: TypeAlias = ProposalDecisionRequest

class DecideProposalResult(TypedDict):
    data: ProposalDecisionResult

class RegisterProposalSafeSubmissionPath(TypedDict):
    id: str

RegisterProposalSafeSubmissionBody: TypeAlias = ProposalSafeSubmissionRequest

class RegisterProposalSafeSubmissionResult(TypedDict):
    data: ProposalSafeSubmissionResult

CompareProposalsBody: TypeAlias = ProposalComparisonRequest

class CompareProposalsResult(TypedDict):
    data: ProposalComparison

class AppendLaunchTimelineEventPath(TypedDict):
    id: str

AppendLaunchTimelineEventBody: TypeAlias = TimelineEventRequest

class AppendLaunchTimelineEventResult(TypedDict):
    data: OperatingSystemEvent

class GetLaunchTimelinePath(TypedDict):
    id: str

class GetLaunchTimelineResult(TypedDict):
    data: LaunchTimeline

class CompleteLaunchTimelineEventPath(TypedDict):
    id: str
    eventId: str

CompleteLaunchTimelineEventBody: TypeAlias = TimelineCompletionRequest

class CompleteLaunchTimelineEventResult(TypedDict):
    data: OperatingSystemEvent

class SeedLaunchWorkspacePath(TypedDict):
    id: str

SeedLaunchWorkspaceBody: TypeAlias = LaunchWorkspaceSeedRequest

class SeedLaunchWorkspaceResult(TypedDict):
    data: LaunchWorkspaceSeed

class SeedIssuerIntentFromCapitalStudyPath(TypedDict):
    id: str

SeedIssuerIntentFromCapitalStudyBody: TypeAlias = CapitalIntentSeedRequest

class SeedIssuerIntentFromCapitalStudyResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: IssuerIntent
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class SeedIssuerIntentFromCapitalStudyResult(TypedDict):
    data: SeedIssuerIntentFromCapitalStudyResultData

class SeedLaunchPlanFromCapitalStudyPath(TypedDict):
    id: str

SeedLaunchPlanFromCapitalStudyBody: TypeAlias = CapitalLaunchSeedRequest

class SeedLaunchPlanFromCapitalStudyResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: LaunchPlan
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class SeedLaunchPlanFromCapitalStudyResult(TypedDict):
    data: SeedLaunchPlanFromCapitalStudyResultData

class ReserveTreasuryFromCapitalStudyPath(TypedDict):
    id: str

ReserveTreasuryFromCapitalStudyBody: TypeAlias = CapitalReservationRequest

class ReserveTreasuryFromCapitalStudyResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: TreasuryBucket
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ReserveTreasuryFromCapitalStudyResult(TypedDict):
    data: ReserveTreasuryFromCapitalStudyResultData

class QueueVenueIndexPath(TypedDict):
    id: str

class QueueVenueIndexBody(TypedDict):
    reason: str

class QueueVenueIndexResult(TypedDict):
    data: OperatingSystemJob

class GetMigrationPlanStatePath(TypedDict):
    id: str

class GetMigrationPlanStateResult(TypedDict):
    data: MigrationPlanStateResult

class AppendMigrationPlanTransitionPath(TypedDict):
    id: str

AppendMigrationPlanTransitionBody: TypeAlias = MigrationTransitionRequest

class AppendMigrationPlanTransitionResult(TypedDict):
    data: MigrationTransitionResult

class CompilePolicyIntentPath(TypedDict):
    id: str

class CompilePolicyIntentBody(TypedDict):
    reason: str

class CompilePolicyIntentResult(TypedDict):
    data: PolicyCompilationResult

CreateStructuredPolicyIntentDraftBody: TypeAlias = StructuredPolicyRequest

class CreateStructuredPolicyIntentDraftResult(TypedDict):
    data: PolicyDraftResult

CheckAutonomyPolicyBody: TypeAlias = PolicyCheckRequest

class CheckAutonomyPolicyResult(TypedDict):
    data: PolicyCheckResult

class RotateDeveloperCredentialPath(TypedDict):
    id: str

class RotateDeveloperCredentialBody(TypedDict):
    reason: str

class RotateDeveloperCredentialResultDataCredential(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: DeveloperCredential
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class RotateDeveloperCredentialResultData(TypedDict):
    credential: RotateDeveloperCredentialResultDataCredential
    secret: str
    priorSecretRevoked: Literal[True]
    secretReturnedOnce: Literal[True]

class RotateDeveloperCredentialResult(TypedDict):
    data: RotateDeveloperCredentialResultData

class GetPartnerPortfolioPath(TypedDict):
    partnerId: str

class GetPartnerPortfolioResult(TypedDict):
    data: PartnerPortfolio

class GetPartnerConsentOptionsQuery(TypedDict):
    partnerId: str
    partnerOrganizationId: str

class GetPartnerConsentOptionsResult(TypedDict):
    data: PartnerConsentOptions

class GetPartnerPreparationContextPath(TypedDict):
    partnerId: str

class GetPartnerPreparationContextQuery(TypedDict):
    issuerOrganizationId: str

class GetPartnerPreparationContextResult(TypedDict):
    data: PartnerPreparationContext

class GetPartnerPreparationReceiptRecoveryPath(TypedDict):
    partnerId: str

class GetPartnerPreparationReceiptRecoveryQuery(TypedDict):
    issuerOrganizationId: str

class GetPartnerPreparationReceiptRecoveryResult(TypedDict):
    data: PartnerPreparationReceiptRecovery

class ListPartnerPreparationsResult(TypedDict):
    data: list[PartnerPreparationInboxEntry]

class ImportPartnerPreparationPath(TypedDict):
    eventId: str

class ImportPartnerPreparationBody(TypedDict):
    reason: str

class ImportPartnerPreparationResult(TypedDict):
    data: PartnerPreparationDecisionResult

class DeclinePartnerPreparationPath(TypedDict):
    eventId: str

class DeclinePartnerPreparationBody(TypedDict):
    reason: str

class DeclinePartnerPreparationResult(TypedDict):
    data: PartnerPreparationDecisionResult

class GetPartnerPreparationStatusPath(TypedDict):
    partnerId: str
    eventId: str

class GetPartnerPreparationStatusQuery(TypedDict):
    issuerOrganizationId: str

class GetPartnerPreparationStatusResult(TypedDict):
    data: PartnerPreparationStatus

class ListPartnerDomainChallengesQuery(TypedDict):
    partnerId: NotRequired[str]
    beforeChallengeId: NotRequired[str]

class ListPartnerDomainChallengesResult(TypedDict):
    data: list[PartnerDomainChallenge]

CreatePartnerDomainChallengeBody: TypeAlias = PartnerDomainChallengeCreateRequest

class CreatePartnerDomainChallengeResult(TypedDict):
    data: PartnerDomainChallenge

class GetPartnerDomainChallengePath(TypedDict):
    id: str

class GetPartnerDomainChallengeResult(TypedDict):
    data: PartnerDomainChallenge

class GetPartnerDomainStatusPath(TypedDict):
    id: str

class GetPartnerDomainStatusResult(TypedDict):
    data: PartnerDomainStatus

class VerifyPartnerDomainChallengePath(TypedDict):
    id: str

class VerifyPartnerDomainChallengeBody(TypedDict):
    reason: str

class VerifyPartnerDomainChallengeResult(TypedDict):
    data: PartnerDomainChallenge

class ProvisionPartnerDomainChallengePath(TypedDict):
    id: str

class ProvisionPartnerDomainChallengeBody(TypedDict):
    reason: str

class ProvisionPartnerDomainChallengeResult(TypedDict):
    data: PartnerDomainChallenge

class RevokePartnerDomainChallengePath(TypedDict):
    id: str

class RevokePartnerDomainChallengeBody(TypedDict):
    reason: str

class RevokePartnerDomainChallengeResult(TypedDict):
    data: PartnerDomainChallenge

class PreparePartnerProposalPath(TypedDict):
    partnerId: str

class PreparePartnerProposalBody(TypedDict):
    issuerOrganizationId: str
    proposal: ProposalWorkspaceInput
    requestExternalDelivery: NotRequired[bool]
    reason: str

class PreparePartnerProposalResult(TypedDict):
    data: PartnerProposalPreparationResult

class RevokePartnerTenantPath(TypedDict):
    id: str

class RevokePartnerTenantBody(TypedDict):
    reason: str

class RevokePartnerTenantResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PartnerTenant
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class RevokePartnerTenantResult(TypedDict):
    data: RevokePartnerTenantResultData

class ListPartnerConsentsResultDataItem(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PartnerIssuerConsent
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class ListPartnerConsentsResult(TypedDict):
    data: list[ListPartnerConsentsResultDataItem]

GrantPartnerConsentBody: TypeAlias = PartnerConsentGrantRequest

class GrantPartnerConsentResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PartnerIssuerConsent
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GrantPartnerConsentResult(TypedDict):
    data: GrantPartnerConsentResultData

class GetPartnerConsentPath(TypedDict):
    id: str

class GetPartnerConsentResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PartnerIssuerConsent
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class GetPartnerConsentResult(TypedDict):
    data: GetPartnerConsentResultData

class RevokePartnerConsentPath(TypedDict):
    id: str

class RevokePartnerConsentBody(TypedDict):
    reason: str

class RevokePartnerConsentResultData(TypedDict):
    id: str
    organizationId: str
    recordType: OperatingSystemRecordType
    version: int
    status: OperatingSystemRecordStatus
    payload: PartnerIssuerConsent
    artifactHash: Hash
    evidenceHashes: list[Hash]
    createdBy: str
    reason: str
    requestId: str
    createdAt: str
    updatedAt: str
    supersedesVersion: NotRequired[int]
    resourceVersion: Hash

class RevokePartnerConsentResult(TypedDict):
    data: RevokePartnerConsentResultData

class ListMarketMakerEvidencePath(TypedDict):
    id: str

class ListMarketMakerEvidenceResult(TypedDict):
    data: list[OperatingSystemEvent]

class IngestMarketMakerEvidencePath(TypedDict):
    id: str

IngestMarketMakerEvidenceBody: TypeAlias = MarketMakerEvidenceRequest

class IngestMarketMakerEvidenceResult(TypedDict):
    data: MarketMakerEvidenceResult

class ListOperatingSystemJobsResult(TypedDict):
    data: list[OperatingSystemJob]

class GetPublicLiquidityPassportPath(TypedDict):
    slug: str

class GetPublicLiquidityPassportResult(TypedDict):
    data: PublicPassportResult

class DownloadPublicLiquidityPassportPath(TypedDict):
    slug: str
    format: Literal["json", "html", "pdf", "csv"]

DownloadPublicLiquidityPassportResult: TypeAlias = Union[LiquidityPassport, bytes]

class DownloadLiquidityPassportVerificationBundlePath(TypedDict):
    slug: str

DownloadLiquidityPassportVerificationBundleResult: TypeAlias = LiquidityPassportVerificationBundle

class GetSharedSimulationStudyPath(TypedDict):
    slug: str

class GetSharedSimulationStudyResult(TypedDict):
    data: SharedSimulationStudy

class GetVerifiedHostBrandResult(TypedDict):
    data: PublicPartnerBrand

class GetVerifiedPartnerBrandLogoPath(TypedDict):
    contentHash: str

GetVerifiedPartnerBrandLogoResult: TypeAlias = bytes

@dataclass(frozen=True)
class LiquidityOsClient(LiquidityOsTransport):
    base_url: str
    organization_id: Optional[str] = None
    access_token: Optional[str] = field(default=None, repr=False)
    timeout_seconds: float = 30.0
    on_response: Optional[ResponseObserver] = field(default=None, repr=False)

    def get_research_planning(self, *, path: GetResearchPlanningPath) -> GetResearchPlanningResult:
        """Read current private Research proposal, clarification and linked study task"""
        return cast(GetResearchPlanningResult, self._request("GET", "/agent-runs/{runId}/research-planning", path=path, accept="application/json"))

    def get_research_progress(self, *, path: GetResearchProgressPath) -> GetResearchProgressResult:
        """Read current private Research child-study progress"""
        return cast(GetResearchProgressResult, self._request("GET", "/agent-runs/{runId}/research-progress", path=path, accept="application/json"))

    def get_research_trial_input(self, *, path: GetResearchTrialInputPath) -> GetResearchTrialInputResult:
        """Inspect the exact immutable inputs of a private Research study"""
        return cast(GetResearchTrialInputResult, self._request("GET", "/agent-runs/{runId}/research-trials/{trialKey}", path=path, accept="application/json"))

    def get_agent_run_result(self, *, path: GetAgentRunResultPath) -> GetAgentRunResultResult:
        """Read and revalidate a saved Health, Proposal Review or Research report"""
        return cast(GetAgentRunResultResult, self._request("GET", "/agent-runs/{runId}/result", path=path, accept="application/json"))

    def get_agent_run_evidence(self, *, path: GetAgentRunEvidencePath) -> GetAgentRunEvidenceResult:
        """Read allowlisted fields from a sealed Health evidence record"""
        return cast(GetAgentRunEvidenceResult, self._request("GET", "/agent-runs/{runId}/evidence/{evidenceId}", path=path, accept="application/json"))

    def apply_agent_run_command(self, *, path: ApplyAgentRunCommandPath, body: ApplyAgentRunCommandBody, idempotency_key: str, if_match: str) -> ApplyAgentRunCommandResult:
        """Cancel remaining work or answer a persisted clarification as its requester"""
        return cast(ApplyAgentRunCommandResult, self._request("POST", "/agent-runs/{runId}/commands", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def start_health_agent_run(self, *, body: StartHealthAgentRunBody, idempotency_key: str) -> StartHealthAgentRunResult:
        """Admit a bounded Health, Proposal Review or Research task against an exact source version"""
        return cast(StartHealthAgentRunResult, self._request("POST", "/agent-runs", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_agent_runs(self, *, query: Optional[ListAgentRunsQuery] = None) -> ListAgentRunsResult:
        """Recover authorized agent task history"""
        return cast(ListAgentRunsResult, self._request("GET", "/agent-runs", query=query, accept="application/json"))

    def get_agent_run(self, *, path: GetAgentRunPath) -> GetAgentRunResult:
        """Read persisted run status and pending clarification"""
        return cast(GetAgentRunResult, self._request("GET", "/agent-runs/{runId}", path=path, accept="application/json"))

    def list_agent_run_events(self, *, path: ListAgentRunEventsPath, query: Optional[ListAgentRunEventsQuery] = None) -> ListAgentRunEventsResult:
        """Read recorded run and checkpoint transitions"""
        return cast(ListAgentRunEventsResult, self._request("GET", "/agent-runs/{runId}/events", path=path, query=query, accept="application/json"))

    def resolve_public_project(self, *, body: ResolvePublicProjectBody) -> ResolvePublicProjectResult:
        """Inspect a supported project using public market sources without a login, vault or payment"""
        return cast(ResolvePublicProjectResult, self._request("POST", "/public/projects/resolve", body=body, content_type="application/json", accept="application/json"))

    def investigate_public_project_liquidity(self, *, body: InvestigatePublicProjectLiquidityBody) -> InvestigatePublicProjectLiquidityResult:
        """Inspect one bounded public reserve-scale liquidity question without a login or payment"""
        return cast(InvestigatePublicProjectLiquidityResult, self._request("POST", "/public/projects/investigate", body=body, content_type="application/json", accept="application/json"))

    def list_saved_projects(self, *, query: Optional[ListSavedProjectsQuery] = None) -> ListSavedProjectsResult:
        """List saved public-project bookmarks in the current workspace"""
        return cast(ListSavedProjectsResult, self._request("GET", "/projects", query=query, accept="application/json"))

    def save_public_project(self, *, body: SavePublicProjectBody, idempotency_key: str) -> SavePublicProjectResult:
        """Save an independently resolved public-project observation"""
        return cast(SavePublicProjectResult, self._request("POST", "/projects", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_saved_project(self, *, path: GetSavedProjectPath) -> GetSavedProjectResult:
        """Read a saved public-project bookmark and its latest observation"""
        return cast(GetSavedProjectResult, self._request("GET", "/projects/{projectId}", path=path, accept="application/json"))

    def refresh_saved_project(self, *, path: RefreshSavedProjectPath, body: RefreshSavedProjectBody, idempotency_key: str, if_match: str) -> RefreshSavedProjectResult:
        """Append a newly resolved public observation to the exact saved project version"""
        return cast(RefreshSavedProjectResult, self._request("POST", "/projects/{projectId}/refresh", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_saved_project_observations(self, *, path: ListSavedProjectObservationsPath, query: Optional[ListSavedProjectObservationsQuery] = None) -> ListSavedProjectObservationsResult:
        """List immutable observation metadata without changing captured evidence"""
        return cast(ListSavedProjectObservationsResult, self._request("GET", "/projects/{projectId}/observations", path=path, query=query, accept="application/json"))

    def get_saved_project_observation(self, *, path: GetSavedProjectObservationPath) -> GetSavedProjectObservationResult:
        """Read the exact immutable public observation version"""
        return cast(GetSavedProjectObservationResult, self._request("GET", "/projects/{projectId}/observations/{version}", path=path, accept="application/json"))

    def list_workspace_plans(self) -> ListWorkspacePlansResult:
        """Inspect configured workspace plan previews without a login or payment"""
        return cast(ListWorkspacePlansResult, self._request("GET", "/public/plans", accept="application/json"))

    def get_public_acp_offering(self) -> GetPublicAcpOfferingResult:
        """Inspect the configured ACP public-analysis offering without a login or payment"""
        return cast(GetPublicAcpOfferingResult, self._request("GET", "/public/acp/offering", accept="application/json"))

    def create_treasury_decision_pack(self, *, body: CreateTreasuryDecisionPackBody, idempotency_key: str) -> CreateTreasuryDecisionPackResult:
        """Prepare a private historical treasury scenario review with its exact project evidence"""
        return cast(CreateTreasuryDecisionPackResult, self._request("POST", "/decision-packs/from-treasury", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def create_research_decision_pack(self, *, body: CreateResearchDecisionPackBody, idempotency_key: str) -> CreateResearchDecisionPackResult:
        """Prepare a private review candidate from an exact Research result"""
        return cast(CreateResearchDecisionPackResult, self._request("POST", "/decision-packs/from-research", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_decision_packs(self, *, query: Optional[ListDecisionPacksQuery] = None) -> ListDecisionPacksResult:
        """List private analysis Decision Packs"""
        return cast(ListDecisionPacksResult, self._request("GET", "/decision-packs", query=query, accept="application/json"))

    def create_decision_pack(self, *, body: CreateDecisionPackBody, idempotency_key: str) -> CreateDecisionPackResult:
        """Create a draft bound to a saved public-project observation"""
        return cast(CreateDecisionPackResult, self._request("POST", "/decision-packs", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_decision_pack(self, *, path: GetDecisionPackPath) -> GetDecisionPackResult:
        """Read the latest Decision Pack version"""
        return cast(GetDecisionPackResult, self._request("GET", "/decision-packs/{packId}", path=path, accept="application/json"))

    def list_decision_pack_versions(self, *, path: ListDecisionPackVersionsPath, query: Optional[ListDecisionPackVersionsQuery] = None) -> ListDecisionPackVersionsResult:
        """List immutable Decision Pack version metadata"""
        return cast(ListDecisionPackVersionsResult, self._request("GET", "/decision-packs/{packId}/versions", path=path, query=query, accept="application/json"))

    def get_decision_pack_version(self, *, path: GetDecisionPackVersionPath) -> GetDecisionPackVersionResult:
        """Read an exact historical Decision Pack version"""
        return cast(GetDecisionPackVersionResult, self._request("GET", "/decision-packs/{packId}/versions/{sequence}", path=path, accept="application/json"))

    def apply_decision_pack_command(self, *, path: ApplyDecisionPackCommandPath, body: ApplyDecisionPackCommandBody, idempotency_key: str, if_match: str) -> ApplyDecisionPackCommandResult:
        """Append a versioned human review action to an exact pack version"""
        return cast(ApplyDecisionPackCommandResult, self._request("POST", "/decision-packs/{packId}/commands", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_treasury_custody_evidence(self, *, query: Optional[ListTreasuryCustodyEvidenceQuery] = None) -> ListTreasuryCustodyEvidenceResult:
        """listTreasuryCustodyEvidence"""
        return cast(ListTreasuryCustodyEvidenceResult, self._request("GET", "/treasury/custody-evidence", query=query, accept="application/json"))

    def admit_treasury_custody_evidence(self, *, body: AdmitTreasuryCustodyEvidenceBody) -> AdmitTreasuryCustodyEvidenceResult:
        """admitTreasuryCustodyEvidence"""
        return cast(AdmitTreasuryCustodyEvidenceResult, self._request("POST", "/treasury/custody-evidence", body=body, content_type="application/json", accept="application/json"))

    def get_treasury_custody_evidence(self, *, path: GetTreasuryCustodyEvidencePath) -> GetTreasuryCustodyEvidenceResult:
        """getTreasuryCustodyEvidence"""
        return cast(GetTreasuryCustodyEvidenceResult, self._request("GET", "/treasury/custody-evidence/{evidenceId}", path=path, accept="application/json"))

    def issue_project_control_challenge(self, *, body: IssueProjectControlChallengeBody, idempotency_key: str) -> IssueProjectControlChallengeResult:
        """issueProjectControlChallenge"""
        return cast(IssueProjectControlChallengeResult, self._request("POST", "/treasury/project-control/challenges", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_project_control_challenge(self, *, path: GetProjectControlChallengePath) -> GetProjectControlChallengeResult:
        """getProjectControlChallenge"""
        return cast(GetProjectControlChallengeResult, self._request("GET", "/treasury/project-control/challenges/{nonce}", path=path, accept="application/json"))

    def accept_project_control_proof(self, *, body: AcceptProjectControlProofBody) -> AcceptProjectControlProofResult:
        """acceptProjectControlProof"""
        return cast(AcceptProjectControlProofResult, self._request("POST", "/treasury/project-control/proofs", body=body, content_type="application/json", accept="application/json"))

    def preview_treasury_reconciliation(self, *, body: PreviewTreasuryReconciliationBody) -> PreviewTreasuryReconciliationResult:
        """previewTreasuryReconciliation"""
        return cast(PreviewTreasuryReconciliationResult, self._request("POST", "/treasury/reconciliation-preview", body=body, content_type="application/json", accept="application/json"))

    def list_treasury_reconciliations(self, *, query: Optional[ListTreasuryReconciliationsQuery] = None) -> ListTreasuryReconciliationsResult:
        """listTreasuryReconciliations"""
        return cast(ListTreasuryReconciliationsResult, self._request("GET", "/treasury/reconciliations", query=query, accept="application/json"))

    def create_treasury_reconciliation(self, *, body: CreateTreasuryReconciliationBody, idempotency_key: str) -> CreateTreasuryReconciliationResult:
        """createTreasuryReconciliation"""
        return cast(CreateTreasuryReconciliationResult, self._request("POST", "/treasury/reconciliations", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_treasury_reconciliation(self, *, path: GetTreasuryReconciliationPath) -> GetTreasuryReconciliationResult:
        """getTreasuryReconciliation"""
        return cast(GetTreasuryReconciliationResult, self._request("GET", "/treasury/reconciliations/{id}", path=path, accept="application/json"))

    def list_treasury_reconciliation_versions(self, *, path: ListTreasuryReconciliationVersionsPath, query: Optional[ListTreasuryReconciliationVersionsQuery] = None) -> ListTreasuryReconciliationVersionsResult:
        """listTreasuryReconciliationVersions"""
        return cast(ListTreasuryReconciliationVersionsResult, self._request("GET", "/treasury/reconciliations/{id}/versions", path=path, query=query, accept="application/json"))

    def get_treasury_reconciliation_version(self, *, path: GetTreasuryReconciliationVersionPath) -> GetTreasuryReconciliationVersionResult:
        """getTreasuryReconciliationVersion"""
        return cast(GetTreasuryReconciliationVersionResult, self._request("GET", "/treasury/reconciliations/{id}/versions/{sequence}", path=path, accept="application/json"))

    def acknowledge_treasury_reconciliation(self, *, path: AcknowledgeTreasuryReconciliationPath, body: AcknowledgeTreasuryReconciliationBody, idempotency_key: str, if_match: str) -> AcknowledgeTreasuryReconciliationResult:
        """acknowledgeTreasuryReconciliation"""
        return cast(AcknowledgeTreasuryReconciliationResult, self._request("POST", "/treasury/reconciliations/{id}/acknowledge", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_treasury_assumptions(self, *, query: Optional[ListTreasuryAssumptionsQuery] = None) -> ListTreasuryAssumptionsResult:
        """listTreasuryAssumptions"""
        return cast(ListTreasuryAssumptionsResult, self._request("GET", "/treasury/assumptions", query=query, accept="application/json"))

    def create_treasury_assumptions(self, *, body: CreateTreasuryAssumptionsBody, idempotency_key: str) -> CreateTreasuryAssumptionsResult:
        """createTreasuryAssumptions"""
        return cast(CreateTreasuryAssumptionsResult, self._request("POST", "/treasury/assumptions", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_treasury_assumptions(self, *, path: GetTreasuryAssumptionsPath) -> GetTreasuryAssumptionsResult:
        """getTreasuryAssumptions"""
        return cast(GetTreasuryAssumptionsResult, self._request("GET", "/treasury/assumptions/{id}", path=path, accept="application/json"))

    def list_treasury_assumptions_versions(self, *, path: ListTreasuryAssumptionsVersionsPath, query: Optional[ListTreasuryAssumptionsVersionsQuery] = None) -> ListTreasuryAssumptionsVersionsResult:
        """listTreasuryAssumptionsVersions"""
        return cast(ListTreasuryAssumptionsVersionsResult, self._request("GET", "/treasury/assumptions/{id}/versions", path=path, query=query, accept="application/json"))

    def get_treasury_assumptions_version(self, *, path: GetTreasuryAssumptionsVersionPath) -> GetTreasuryAssumptionsVersionResult:
        """getTreasuryAssumptionsVersion"""
        return cast(GetTreasuryAssumptionsVersionResult, self._request("GET", "/treasury/assumptions/{id}/versions/{sequence}", path=path, accept="application/json"))

    def revise_treasury_assumptions(self, *, path: ReviseTreasuryAssumptionsPath, body: ReviseTreasuryAssumptionsBody, idempotency_key: str, if_match: str) -> ReviseTreasuryAssumptionsResult:
        """reviseTreasuryAssumptions"""
        return cast(ReviseTreasuryAssumptionsResult, self._request("POST", "/treasury/assumptions/{id}/revisions", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_treasury_projections(self, *, query: Optional[ListTreasuryProjectionsQuery] = None) -> ListTreasuryProjectionsResult:
        """listTreasuryProjections"""
        return cast(ListTreasuryProjectionsResult, self._request("GET", "/treasury/projections", query=query, accept="application/json"))

    def create_treasury_projection(self, *, body: CreateTreasuryProjectionBody, idempotency_key: str) -> CreateTreasuryProjectionResult:
        """createTreasuryProjection"""
        return cast(CreateTreasuryProjectionResult, self._request("POST", "/treasury/projections", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_treasury_projection(self, *, path: GetTreasuryProjectionPath) -> GetTreasuryProjectionResult:
        """getTreasuryProjection"""
        return cast(GetTreasuryProjectionResult, self._request("GET", "/treasury/projections/{id}", path=path, accept="application/json"))

    def search_discovered_projects(self, *, query: SearchDiscoveredProjectsQuery) -> SearchDiscoveredProjectsResult:
        """Search supported public Virtuals project identities"""
        return cast(SearchDiscoveredProjectsResult, self._request("GET", "/public/discovery/search", query=query, accept="application/json"))

    def get_discovered_project_market(self, *, path: GetDiscoveredProjectMarketPath) -> GetDiscoveredProjectMarketResult:
        """Read provider-reported project pools and market figures"""
        return cast(GetDiscoveredProjectMarketResult, self._request("GET", "/public/discovery/market/{id}", path=path, accept="application/json"))

    def get_market_discovery_capabilities(self) -> GetMarketDiscoveryCapabilitiesResult:
        """Read configured research capability availability"""
        return cast(GetMarketDiscoveryCapabilitiesResult, self._request("GET", "/public/discovery/capabilities", accept="application/json"))

    def get_workflow_context(self) -> GetWorkflowContextResult:
        """List authorized vault choices and saved-research availability"""
        return cast(GetWorkflowContextResult, self._request("GET", "/workflows/context", accept="application/json"))

    def list_completed_workflow_runs(self, *, query: Optional[ListCompletedWorkflowRunsQuery] = None) -> ListCompletedWorkflowRunsResult:
        """List completed research saved for the current workspace and reader"""
        return cast(ListCompletedWorkflowRunsResult, self._request("GET", "/workflows/runs", query=query, accept="application/json"))

    def get_completed_workflow_run(self, *, path: GetCompletedWorkflowRunPath) -> GetCompletedWorkflowRunResult:
        """Read one immutable research result saved for the current reader"""
        return cast(GetCompletedWorkflowRunResult, self._request("GET", "/workflows/runs/{id}", path=path, accept="application/json"))

    def run_workflow_research(self, *, body: RunWorkflowResearchBody) -> RunWorkflowResearchResult:
        """Complete a bounded read-only liquidity research question"""
        return cast(RunWorkflowResearchResult, self._request("POST", "/workflows/run", body=body, content_type="application/json", accept="application/json"))

    def list_saved_virtuals_projects(self, *, query: Optional[ListSavedVirtualsProjectsQuery] = None) -> ListSavedVirtualsProjectsResult:
        """List workspace Virtuals directory bookmarks"""
        return cast(ListSavedVirtualsProjectsResult, self._request("GET", "/virtuals-projects", query=query, accept="application/json"))

    def save_virtuals_project(self, *, body: SaveVirtualsProjectBody) -> SaveVirtualsProjectResult:
        """Save an independently resolved Virtuals directory bookmark"""
        return cast(SaveVirtualsProjectResult, self._request("POST", "/virtuals-projects", body=body, content_type="application/json", accept="application/json"))

    def get_saved_virtuals_project(self, *, path: GetSavedVirtualsProjectPath) -> GetSavedVirtualsProjectResult:
        """Read a workspace Virtuals directory bookmark"""
        return cast(GetSavedVirtualsProjectResult, self._request("GET", "/virtuals-projects/{id}", path=path, accept="application/json"))

    def remove_saved_virtuals_project(self, *, path: RemoveSavedVirtualsProjectPath, body: RemoveSavedVirtualsProjectBody) -> RemoveSavedVirtualsProjectResult:
        """Remove the exact reviewed Virtuals directory bookmark generation"""
        return cast(RemoveSavedVirtualsProjectResult, self._request("DELETE", "/virtuals-projects/{id}", path=path, body=body, content_type="application/json", accept="application/json"))

    def list_treasury_ledger_entry_versions(self, *, path: ListTreasuryLedgerEntryVersionsPath, query: Optional[ListTreasuryLedgerEntryVersionsQuery] = None) -> ListTreasuryLedgerEntryVersionsResult:
        """List immutable versions of a treasury ledger entry"""
        return cast(ListTreasuryLedgerEntryVersionsResult, self._request("GET", "/treasury-entries/{id}/versions", path=path, query=query, accept="application/json"))

    def get_proposal_workspace_review(self, *, path: GetProposalWorkspaceReviewPath, query: GetProposalWorkspaceReviewQuery) -> GetProposalWorkspaceReviewResult:
        """Read a resource-version-bound proposal review snapshot"""
        return cast(GetProposalWorkspaceReviewResult, self._request("GET", "/proposals/{id}/review", path=path, query=query, accept="application/json"))

    def list_intents(self, *, query: Optional[ListIntentsQuery] = None) -> ListIntentsResult:
        """List issuer intents"""
        return cast(ListIntentsResult, self._request("GET", "/intents", query=query, accept="application/json"))

    def create_intents(self, *, body: CreateIntentsBody, idempotency_key: str) -> CreateIntentsResult:
        """Create issuer intents"""
        return cast(CreateIntentsResult, self._request("POST", "/intents", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_intents(self, *, path: GetIntentsPath) -> GetIntentsResult:
        """Get one issuer intents aggregate"""
        return cast(GetIntentsResult, self._request("GET", "/intents/{id}", path=path, accept="application/json"))

    def supersede_intents(self, *, path: SupersedeIntentsPath, body: SupersedeIntentsBody, idempotency_key: str, if_match: str) -> SupersedeIntentsResult:
        """Supersede an intent and recompute immutable deterministic capital evidence"""
        return cast(SupersedeIntentsResult, self._request("PATCH", "/intents/{id}", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_studies(self, *, query: Optional[ListStudiesQuery] = None) -> ListStudiesResult:
        """List simulation studies"""
        return cast(ListStudiesResult, self._request("GET", "/studies", query=query, accept="application/json"))

    def create_studies(self, *, body: CreateStudiesBody, idempotency_key: str) -> CreateStudiesResult:
        """Create simulation studies"""
        return cast(CreateStudiesResult, self._request("POST", "/studies", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_studies(self, *, path: GetStudiesPath) -> GetStudiesResult:
        """Get one simulation studies aggregate"""
        return cast(GetStudiesResult, self._request("GET", "/studies/{id}", path=path, accept="application/json"))

    def list_study_shares(self, *, query: Optional[ListStudySharesQuery] = None) -> ListStudySharesResult:
        """List revocable simulation-study shares"""
        return cast(ListStudySharesResult, self._request("GET", "/study-shares", query=query, accept="application/json"))

    def get_study_shares(self, *, path: GetStudySharesPath) -> GetStudySharesResult:
        """Get one revocable simulation-study shares aggregate"""
        return cast(GetStudySharesResult, self._request("GET", "/study-shares/{id}", path=path, accept="application/json"))

    def list_strategies(self, *, query: Optional[ListStrategiesQuery] = None) -> ListStrategiesResult:
        """List strategy definitions"""
        return cast(ListStrategiesResult, self._request("GET", "/strategies", query=query, accept="application/json"))

    def create_strategies(self, *, body: CreateStrategiesBody, idempotency_key: str) -> CreateStrategiesResult:
        """Create strategy definitions"""
        return cast(CreateStrategiesResult, self._request("POST", "/strategies", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_strategies(self, *, path: GetStrategiesPath) -> GetStrategiesResult:
        """Get one strategy definitions aggregate"""
        return cast(GetStrategiesResult, self._request("GET", "/strategies/{id}", path=path, accept="application/json"))

    def supersede_strategies(self, *, path: SupersedeStrategiesPath, body: SupersedeStrategiesBody, idempotency_key: str, if_match: str) -> SupersedeStrategiesResult:
        """Supersede a declarative strategy only after deterministic compilation"""
        return cast(SupersedeStrategiesResult, self._request("PATCH", "/strategies/{id}", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_proposals(self, *, query: Optional[ListProposalsQuery] = None) -> ListProposalsResult:
        """List decision workspaces"""
        return cast(ListProposalsResult, self._request("GET", "/proposals", query=query, accept="application/json"))

    def create_proposals(self, *, body: CreateProposalsBody, idempotency_key: str) -> CreateProposalsResult:
        """Create a decision packet with zero server-recorded approvals"""
        return cast(CreateProposalsResult, self._request("POST", "/proposals", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_proposals(self, *, path: GetProposalsPath) -> GetProposalsResult:
        """Get one decision workspaces aggregate"""
        return cast(GetProposalsResult, self._request("GET", "/proposals/{id}", path=path, accept="application/json"))

    def list_launch_plans(self, *, query: Optional[ListLaunchPlansQuery] = None) -> ListLaunchPlansResult:
        """List launch plans"""
        return cast(ListLaunchPlansResult, self._request("GET", "/launch-plans", query=query, accept="application/json"))

    def create_launch_plans(self, *, body: CreateLaunchPlansBody, idempotency_key: str) -> CreateLaunchPlansResult:
        """Create launch plans"""
        return cast(CreateLaunchPlansResult, self._request("POST", "/launch-plans", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_launch_plans(self, *, path: GetLaunchPlansPath) -> GetLaunchPlansResult:
        """Get one launch plans aggregate"""
        return cast(GetLaunchPlansResult, self._request("GET", "/launch-plans/{id}", path=path, accept="application/json"))

    def list_unlock_impacts(self, *, query: Optional[ListUnlockImpactsQuery] = None) -> ListUnlockImpactsResult:
        """List unlock impact studies"""
        return cast(ListUnlockImpactsResult, self._request("GET", "/unlock-impacts", query=query, accept="application/json"))

    def create_unlock_impacts(self, *, body: CreateUnlockImpactsBody, idempotency_key: str) -> CreateUnlockImpactsResult:
        """Create a correlation-aware unlock study and queue four explicit downstream materializations"""
        return cast(CreateUnlockImpactsResult, self._request("POST", "/unlock-impacts", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_unlock_impacts(self, *, path: GetUnlockImpactsPath) -> GetUnlockImpactsResult:
        """Get one unlock impact studies aggregate"""
        return cast(GetUnlockImpactsResult, self._request("GET", "/unlock-impacts/{id}", path=path, accept="application/json"))

    def list_scores(self, *, query: Optional[ListScoresQuery] = None) -> ListScoresResult:
        """List market quality scores"""
        return cast(ListScoresResult, self._request("GET", "/scores", query=query, accept="application/json"))

    def create_scores(self, *, body: CreateScoresBody, idempotency_key: str) -> CreateScoresResult:
        """Create market quality scores"""
        return cast(CreateScoresResult, self._request("POST", "/scores", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_scores(self, *, path: GetScoresPath) -> GetScoresResult:
        """Get one market quality scores aggregate"""
        return cast(GetScoresResult, self._request("GET", "/scores/{id}", path=path, accept="application/json"))

    def list_attributions(self, *, query: Optional[ListAttributionsQuery] = None) -> ListAttributionsResult:
        """List execution attributions"""
        return cast(ListAttributionsResult, self._request("GET", "/attributions", query=query, accept="application/json"))

    def create_attributions(self, *, body: CreateAttributionsBody, idempotency_key: str) -> CreateAttributionsResult:
        """Create execution attributions"""
        return cast(CreateAttributionsResult, self._request("POST", "/attributions", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_attributions(self, *, path: GetAttributionsPath) -> GetAttributionsResult:
        """Get one execution attributions aggregate"""
        return cast(GetAttributionsResult, self._request("GET", "/attributions/{id}", path=path, accept="application/json"))

    def list_anomalies(self, *, query: Optional[ListAnomaliesQuery] = None) -> ListAnomaliesResult:
        """List anomalies"""
        return cast(ListAnomaliesResult, self._request("GET", "/anomalies", query=query, accept="application/json"))

    def create_anomalies(self, *, body: CreateAnomaliesBody, idempotency_key: str) -> CreateAnomaliesResult:
        """Create anomalies"""
        return cast(CreateAnomaliesResult, self._request("POST", "/anomalies", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_anomalies(self, *, path: GetAnomaliesPath) -> GetAnomaliesResult:
        """Get one anomalies aggregate"""
        return cast(GetAnomaliesResult, self._request("GET", "/anomalies/{id}", path=path, accept="application/json"))

    def list_treasury_entries(self, *, query: Optional[ListTreasuryEntriesQuery] = None) -> ListTreasuryEntriesResult:
        """List treasury ledger entries"""
        return cast(ListTreasuryEntriesResult, self._request("GET", "/treasury-entries", query=query, accept="application/json"))

    def create_treasury_entries(self, *, body: CreateTreasuryEntriesBody, idempotency_key: str) -> CreateTreasuryEntriesResult:
        """Append a fresh signed oracle-bound economic capital container"""
        return cast(CreateTreasuryEntriesResult, self._request("POST", "/treasury-entries", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_treasury_entries(self, *, path: GetTreasuryEntriesPath) -> GetTreasuryEntriesResult:
        """Get one treasury ledger entries aggregate"""
        return cast(GetTreasuryEntriesResult, self._request("GET", "/treasury-entries/{id}", path=path, accept="application/json"))

    def list_capital_requirements(self, *, query: Optional[ListCapitalRequirementsQuery] = None) -> ListCapitalRequirementsResult:
        """List capital requirement studies"""
        return cast(ListCapitalRequirementsResult, self._request("GET", "/capital-requirements", query=query, accept="application/json"))

    def create_capital_requirements(self, *, body: CreateCapitalRequirementsBody, idempotency_key: str) -> CreateCapitalRequirementsResult:
        """Create capital requirement studies"""
        return cast(CreateCapitalRequirementsResult, self._request("POST", "/capital-requirements", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_capital_requirements(self, *, path: GetCapitalRequirementsPath) -> GetCapitalRequirementsResult:
        """Get one capital requirement studies aggregate"""
        return cast(GetCapitalRequirementsResult, self._request("GET", "/capital-requirements/{id}", path=path, accept="application/json"))

    def list_treasury_stress_tests(self, *, query: Optional[ListTreasuryStressTestsQuery] = None) -> ListTreasuryStressTestsResult:
        """List treasury stress studies"""
        return cast(ListTreasuryStressTestsResult, self._request("GET", "/treasury-stress-tests", query=query, accept="application/json"))

    def create_treasury_stress_tests(self, *, body: CreateTreasuryStressTestsBody, idempotency_key: str) -> CreateTreasuryStressTestsResult:
        """Run all seven deterministic shocks using the server-side ledger, launch unlocks, and current policy"""
        return cast(CreateTreasuryStressTestsResult, self._request("POST", "/treasury-stress-tests", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_treasury_stress_tests(self, *, path: GetTreasuryStressTestsPath) -> GetTreasuryStressTestsResult:
        """Get one treasury stress studies aggregate"""
        return cast(GetTreasuryStressTestsResult, self._request("GET", "/treasury-stress-tests/{id}", path=path, accept="application/json"))

    def list_venues(self, *, query: Optional[ListVenuesQuery] = None) -> ListVenuesResult:
        """List venue profiles"""
        return cast(ListVenuesResult, self._request("GET", "/venues", query=query, accept="application/json"))

    def create_venues(self, *, body: CreateVenuesBody, idempotency_key: str) -> CreateVenuesResult:
        """Create venue profiles"""
        return cast(CreateVenuesResult, self._request("POST", "/venues", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_venues(self, *, path: GetVenuesPath) -> GetVenuesResult:
        """Get one venue profiles aggregate"""
        return cast(GetVenuesResult, self._request("GET", "/venues/{id}", path=path, accept="application/json"))

    def supersede_venues(self, *, path: SupersedeVenuesPath, body: SupersedeVenuesBody, idempotency_key: str, if_match: str) -> SupersedeVenuesResult:
        """Supersede validation-only read-profile metadata; write adapters require a separate signed release"""
        return cast(SupersedeVenuesResult, self._request("PATCH", "/venues/{id}", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_venue_observations(self, *, query: Optional[ListVenueObservationsQuery] = None) -> ListVenueObservationsResult:
        """List venue observations"""
        return cast(ListVenueObservationsResult, self._request("GET", "/venue-observations", query=query, accept="application/json"))

    def get_venue_observations(self, *, path: GetVenueObservationsPath) -> GetVenueObservationsResult:
        """Get one venue observations aggregate"""
        return cast(GetVenueObservationsResult, self._request("GET", "/venue-observations/{id}", path=path, accept="application/json"))

    def list_allocation_plans(self, *, query: Optional[ListAllocationPlansQuery] = None) -> ListAllocationPlansResult:
        """List multi-venue allocation plans"""
        return cast(ListAllocationPlansResult, self._request("GET", "/allocation-plans", query=query, accept="application/json"))

    def create_allocation_plans(self, *, body: CreateAllocationPlansBody, idempotency_key: str) -> CreateAllocationPlansResult:
        """Create multi-venue allocation plans"""
        return cast(CreateAllocationPlansResult, self._request("POST", "/allocation-plans", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_allocation_plans(self, *, path: GetAllocationPlansPath) -> GetAllocationPlansResult:
        """Get one multi-venue allocation plans aggregate"""
        return cast(GetAllocationPlansResult, self._request("GET", "/allocation-plans/{id}", path=path, accept="application/json"))

    def list_migration_plans(self, *, query: Optional[ListMigrationPlansQuery] = None) -> ListMigrationPlansResult:
        """List liquidity migration plans"""
        return cast(ListMigrationPlansResult, self._request("GET", "/migration-plans", query=query, accept="application/json"))

    def create_migration_plans(self, *, body: CreateMigrationPlansBody, idempotency_key: str) -> CreateMigrationPlansResult:
        """Create liquidity migration plans"""
        return cast(CreateMigrationPlansResult, self._request("POST", "/migration-plans", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_migration_plans(self, *, path: GetMigrationPlansPath) -> GetMigrationPlansResult:
        """Get one liquidity migration plans aggregate"""
        return cast(GetMigrationPlansResult, self._request("GET", "/migration-plans/{id}", path=path, accept="application/json"))

    def list_autonomy_policies(self, *, query: Optional[ListAutonomyPoliciesQuery] = None) -> ListAutonomyPoliciesResult:
        """List autonomy policies"""
        return cast(ListAutonomyPoliciesResult, self._request("GET", "/autonomy-policies", query=query, accept="application/json"))

    def create_autonomy_policies(self, *, body: CreateAutonomyPoliciesBody, idempotency_key: str, if_match: Optional[str] = None) -> CreateAutonomyPoliciesResult:
        """Create or expand autonomy using server-reconciled exact v2 Safe-envelope evidence"""
        return cast(CreateAutonomyPoliciesResult, self._request("POST", "/autonomy-policies", body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_autonomy_policies(self, *, path: GetAutonomyPoliciesPath) -> GetAutonomyPoliciesResult:
        """Get one autonomy policies aggregate"""
        return cast(GetAutonomyPoliciesResult, self._request("GET", "/autonomy-policies/{id}", path=path, accept="application/json"))

    def supersede_autonomy_policies(self, *, path: SupersedeAutonomyPoliciesPath, body: SupersedeAutonomyPoliciesBody, idempotency_key: str, if_match: str) -> SupersedeAutonomyPoliciesResult:
        """Immediately pause, revoke, or narrow policy authority; expansion uses the typed Safe workflow"""
        return cast(SupersedeAutonomyPoliciesResult, self._request("PATCH", "/autonomy-policies/{id}", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_policy_intent_drafts(self, *, query: Optional[ListPolicyIntentDraftsQuery] = None) -> ListPolicyIntentDraftsResult:
        """List natural-language policy drafts"""
        return cast(ListPolicyIntentDraftsResult, self._request("GET", "/policy-intent-drafts", query=query, accept="application/json"))

    def create_policy_intent_drafts(self, *, body: CreatePolicyIntentDraftsBody, idempotency_key: str) -> CreatePolicyIntentDraftsResult:
        """Create natural-language policy drafts"""
        return cast(CreatePolicyIntentDraftsResult, self._request("POST", "/policy-intent-drafts", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_policy_intent_drafts(self, *, path: GetPolicyIntentDraftsPath) -> GetPolicyIntentDraftsResult:
        """Get one natural-language policy drafts aggregate"""
        return cast(GetPolicyIntentDraftsResult, self._request("GET", "/policy-intent-drafts/{id}", path=path, accept="application/json"))

    def list_quote_sets(self, *, query: Optional[ListQuoteSetsQuery] = None) -> ListQuoteSetsResult:
        """List protected execution quote sets"""
        return cast(ListQuoteSetsResult, self._request("GET", "/quote-sets", query=query, accept="application/json"))

    def admit_protected_execution_quote_set(self, *, body: AdmitProtectedExecutionQuoteSetBody, idempotency_key: str, if_match: str) -> AdmitProtectedExecutionQuoteSetResult:
        """Append signed provider quotes to an immutable policy-bound quote request"""
        return cast(AdmitProtectedExecutionQuoteSetResult, self._request("POST", "/quote-sets", body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_quote_sets(self, *, path: GetQuoteSetsPath) -> GetQuoteSetsResult:
        """Get one protected execution quote sets aggregate"""
        return cast(GetQuoteSetsResult, self._request("GET", "/quote-sets/{id}", path=path, accept="application/json"))

    def list_protected_execution_plans(self, *, query: Optional[ListProtectedExecutionPlansQuery] = None) -> ListProtectedExecutionPlansResult:
        """List protected execution plans"""
        return cast(ListProtectedExecutionPlansResult, self._request("GET", "/protected-execution-plans", query=query, accept="application/json"))

    def prepare_protected_execution_plan(self, *, body: PrepareProtectedExecutionPlanBody, idempotency_key: str) -> PrepareProtectedExecutionPlanResult:
        """Prepare typed child legs under the quote request current immutable policy binding"""
        return cast(PrepareProtectedExecutionPlanResult, self._request("POST", "/protected-execution-plans", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_protected_execution_plans(self, *, path: GetProtectedExecutionPlansPath) -> GetProtectedExecutionPlansResult:
        """Get one protected execution plans aggregate"""
        return cast(GetProtectedExecutionPlansResult, self._request("GET", "/protected-execution-plans/{id}", path=path, accept="application/json"))

    def list_developer_credentials(self, *, query: Optional[ListDeveloperCredentialsQuery] = None) -> ListDeveloperCredentialsResult:
        """List developer credentials"""
        return cast(ListDeveloperCredentialsResult, self._request("GET", "/developer-credentials", query=query, accept="application/json"))

    def create_developer_credentials(self, *, body: CreateDeveloperCredentialsBody, idempotency_key: str) -> CreateDeveloperCredentialsResult:
        """Create a hashed developer credential and return its secret once"""
        return cast(CreateDeveloperCredentialsResult, self._request("POST", "/developer-credentials", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_developer_credentials(self, *, path: GetDeveloperCredentialsPath) -> GetDeveloperCredentialsResult:
        """Get one developer credentials aggregate"""
        return cast(GetDeveloperCredentialsResult, self._request("GET", "/developer-credentials/{id}", path=path, accept="application/json"))

    def supersede_developer_credentials(self, *, path: SupersedeDeveloperCredentialsPath, body: SupersedeDeveloperCredentialsBody, idempotency_key: str, if_match: str) -> SupersedeDeveloperCredentialsResult:
        """Immediately revoke a developer credential"""
        return cast(SupersedeDeveloperCredentialsResult, self._request("PATCH", "/developer-credentials/{id}", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_webhooks(self, *, query: Optional[ListWebhooksQuery] = None) -> ListWebhooksResult:
        """List webhook subscriptions"""
        return cast(ListWebhooksResult, self._request("GET", "/webhooks", query=query, accept="application/json"))

    def create_webhooks(self, *, body: CreateWebhooksBody, idempotency_key: str) -> CreateWebhooksResult:
        """Create a signed webhook and return its signing secret once"""
        return cast(CreateWebhooksResult, self._request("POST", "/webhooks", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_webhooks(self, *, path: GetWebhooksPath) -> GetWebhooksResult:
        """Get one webhook subscriptions aggregate"""
        return cast(GetWebhooksResult, self._request("GET", "/webhooks/{id}", path=path, accept="application/json"))

    def supersede_webhooks(self, *, path: SupersedeWebhooksPath, body: SupersedeWebhooksBody, idempotency_key: str, if_match: str) -> SupersedeWebhooksResult:
        """Immediately pause or revoke a webhook subscription"""
        return cast(SupersedeWebhooksResult, self._request("PATCH", "/webhooks/{id}", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_strategy_packages(self, *, query: Optional[ListStrategyPackagesQuery] = None) -> ListStrategyPackagesResult:
        """List curated strategy packages"""
        return cast(ListStrategyPackagesResult, self._request("GET", "/strategy-packages", query=query, accept="application/json"))

    def create_strategy_package_candidate(self, *, body: CreateStrategyPackageCandidateBody, idempotency_key: str) -> CreateStrategyPackageCandidateResult:
        """Create an immutable declarative candidate restricted to Digital Twin use"""
        return cast(CreateStrategyPackageCandidateResult, self._request("POST", "/strategy-packages", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_strategy_packages(self, *, path: GetStrategyPackagesPath) -> GetStrategyPackagesResult:
        """Get one curated strategy packages aggregate"""
        return cast(GetStrategyPackagesResult, self._request("GET", "/strategy-packages/{id}", path=path, accept="application/json"))

    def list_partners(self, *, query: Optional[ListPartnersQuery] = None) -> ListPartnersResult:
        """List white-label partner tenants"""
        return cast(ListPartnersResult, self._request("GET", "/partners", query=query, accept="application/json"))

    def create_verified_partner_tenant(self, *, body: CreateVerifiedPartnerTenantBody, idempotency_key: str) -> CreateVerifiedPartnerTenantResult:
        """Bind brand configuration to fresh signed exact-domain verifier evidence"""
        return cast(CreateVerifiedPartnerTenantResult, self._request("POST", "/partners", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_partners(self, *, path: GetPartnersPath) -> GetPartnersResult:
        """Get one white-label partner tenants aggregate"""
        return cast(GetPartnersResult, self._request("GET", "/partners/{id}", path=path, accept="application/json"))

    def update_partner_configuration(self, *, path: UpdatePartnerConfigurationPath, body: UpdatePartnerConfigurationBody, idempotency_key: str, if_match: str) -> UpdatePartnerConfigurationResult:
        """Append an explicitly reviewed partner generation after current domain verification"""
        return cast(UpdatePartnerConfigurationResult, self._request("PATCH", "/partners/{id}", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_market_maker_mandates(self, *, query: Optional[ListMarketMakerMandatesQuery] = None) -> ListMarketMakerMandatesResult:
        """List market-maker mandates"""
        return cast(ListMarketMakerMandatesResult, self._request("GET", "/market-maker-mandates", query=query, accept="application/json"))

    def create_market_maker_mandate(self, *, body: CreateMarketMakerMandateBody, idempotency_key: str) -> CreateMarketMakerMandateResult:
        """Create a monitoring-only market-maker mandate with an AMM comparison benchmark"""
        return cast(CreateMarketMakerMandateResult, self._request("POST", "/market-maker-mandates", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_market_maker_mandates(self, *, path: GetMarketMakerMandatesPath) -> GetMarketMakerMandatesResult:
        """Get one market-maker mandates aggregate"""
        return cast(GetMarketMakerMandatesResult, self._request("GET", "/market-maker-mandates/{id}", path=path, accept="application/json"))

    def supersede_market_maker_mandates(self, *, path: SupersedeMarketMakerMandatesPath, body: SupersedeMarketMakerMandatesBody, idempotency_key: str, if_match: str) -> SupersedeMarketMakerMandatesResult:
        """Pause or revoke a mandate without replacing signed economics"""
        return cast(SupersedeMarketMakerMandatesResult, self._request("PATCH", "/market-maker-mandates/{id}", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_incentive_programs(self, *, query: Optional[ListIncentiveProgramsQuery] = None) -> ListIncentiveProgramsResult:
        """List incentive programs"""
        return cast(ListIncentiveProgramsResult, self._request("GET", "/incentive-programs", query=query, accept="application/json"))

    def optimize_incentive_program(self, *, body: OptimizeIncentiveProgramBody, idempotency_key: str) -> OptimizeIncentiveProgramResult:
        """Measure an incentive program against frozen baseline evidence and prepare a non-executing review workflow"""
        return cast(OptimizeIncentiveProgramResult, self._request("POST", "/incentive-programs", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_incentive_programs(self, *, path: GetIncentiveProgramsPath) -> GetIncentiveProgramsResult:
        """Get one incentive programs aggregate"""
        return cast(GetIncentiveProgramsResult, self._request("GET", "/incentive-programs/{id}", path=path, accept="application/json"))

    def supersede_incentive_programs(self, *, path: SupersedeIncentiveProgramsPath, body: SupersedeIncentiveProgramsBody, idempotency_key: str, if_match: str) -> SupersedeIncentiveProgramsResult:
        """Revoke an incentive-program result without replacing its evidence"""
        return cast(SupersedeIncentiveProgramsResult, self._request("PATCH", "/incentive-programs/{id}", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_passports(self, *, query: Optional[ListPassportsQuery] = None) -> ListPassportsResult:
        """List liquidity passports"""
        return cast(ListPassportsResult, self._request("GET", "/passports", query=query, accept="application/json"))

    def publish_liquidity_passport(self, *, body: PublishLiquidityPassportBody, idempotency_key: str, if_match: Optional[str] = None) -> PublishLiquidityPassportResult:
        """Publish issuer-signed claims recomputed from exact current server evidence"""
        return cast(PublishLiquidityPassportResult, self._request("POST", "/passports", body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_passports(self, *, path: GetPassportsPath) -> GetPassportsResult:
        """Get one liquidity passports aggregate"""
        return cast(GetPassportsResult, self._request("GET", "/passports/{id}", path=path, accept="application/json"))

    def get_operating_system_open_api(self) -> GetOperatingSystemOpenApiResult:
        """Download the checked-in v2 OpenAPI contract"""
        return cast(GetOperatingSystemOpenApiResult, self._request("GET", "/openapi.json", accept="application/json"))

    def get_operating_system_status(self) -> GetOperatingSystemStatusResult:
        """Read fail-closed v2 service readiness"""
        return cast(GetOperatingSystemStatusResult, self._request("GET", "/status", accept="application/json"))

    def issue_operating_system_oauth_token(self, *, body: IssueOperatingSystemOAuthTokenBody, client_id: str, client_secret: str) -> IssueOperatingSystemOAuthTokenResult:
        """Exchange OAuth client credentials for a scoped one-hour token"""
        return cast(IssueOperatingSystemOAuthTokenResult, self._request("POST", "/oauth/token", body=body, basic_auth=(client_id, client_secret), content_type="application/x-www-form-urlencoded", accept="application/json"))

    def activate_market_quality_score(self, *, path: ActivateMarketQualityScorePath, body: ActivateMarketQualityScoreBody, idempotency_key: str, if_match: str) -> ActivateMarketQualityScoreResult:
        """Issuer-review and activate an available immutable analyst score draft"""
        return cast(ActivateMarketQualityScoreResult, self._request("POST", "/scores/{id}/activate", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def create_protected_execution_quote_request(self, *, body: CreateProtectedExecutionQuoteRequestBody, idempotency_key: str) -> CreateProtectedExecutionQuoteRequestResult:
        """Create a server-derived quote request bound to the current immutable AutonomyPolicy generation"""
        return cast(CreateProtectedExecutionQuoteRequestResult, self._request("POST", "/quote-requests", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def admit_protected_execution_quotes_for_request(self, *, path: AdmitProtectedExecutionQuotesForRequestPath, body: AdmitProtectedExecutionQuotesForRequestBody, idempotency_key: str, if_match: str) -> AdmitProtectedExecutionQuotesForRequestResult:
        """Verify and append current-generation signed provider quotes"""
        return cast(AdmitProtectedExecutionQuotesForRequestResult, self._request("POST", "/quote-requests/{id}/quotes", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_protected_execution_plan_state(self, *, path: GetProtectedExecutionPlanStatePath) -> GetProtectedExecutionPlanStateResult:
        """Read materialized child-leg accounting and its deterministic state hash"""
        return cast(GetProtectedExecutionPlanStateResult, self._request("GET", "/protected-execution-plans/{id}/state", path=path, accept="application/json"))

    def append_protected_execution_leg_transition(self, *, path: AppendProtectedExecutionLegTransitionPath, body: AppendProtectedExecutionLegTransitionBody, idempotency_key: str, if_match: str) -> AppendProtectedExecutionLegTransitionResult:
        """Request a server-verified typed lifecycle transition without accepting client evidence"""
        return cast(AppendProtectedExecutionLegTransitionResult, self._request("POST", "/protected-execution-plans/{id}/transitions", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def refresh_treasury_ledger_entry(self, *, path: RefreshTreasuryLedgerEntryPath, body: RefreshTreasuryLedgerEntryBody, idempotency_key: str, if_match: str) -> RefreshTreasuryLedgerEntryResult:
        """Append a fresh signed observation for an existing immutable treasury container identity"""
        return cast(RefreshTreasuryLedgerEntryResult, self._request("POST", "/treasury-entries/{id}/refresh", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def retire_treasury_ledger_entry(self, *, path: RetireTreasuryLedgerEntryPath, body: RetireTreasuryLedgerEntryBody, idempotency_key: str, if_match: str) -> RetireTreasuryLedgerEntryResult:
        """Append a revoked treasury-container generation with immutable retirement evidence"""
        return cast(RetireTreasuryLedgerEntryResult, self._request("POST", "/treasury-entries/{id}/retire", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_operating_system_workspace(self) -> GetOperatingSystemWorkspaceResult:
        """Get all release-train availability and aggregate counts"""
        return cast(GetOperatingSystemWorkspaceResult, self._request("GET", "/workspace", accept="application/json"))

    def list_qualified_vaults_v2(self, *, query: Optional[ListQualifiedVaultsV2Query] = None) -> ListQualifiedVaultsV2Result:
        """List tenant-isolated qualified vault metadata projected from authoritative v1 custody records"""
        return cast(ListQualifiedVaultsV2Result, self._request("GET", "/vaults", query=query, accept="application/json"))

    def get_qualified_vault_v2(self, *, path: GetQualifiedVaultV2Path) -> GetQualifiedVaultV2Result:
        """Read one qualified vault and immutable deployment/control evidence"""
        return cast(GetQualifiedVaultV2Result, self._request("GET", "/vaults/{id}", path=path, accept="application/json"))

    def list_execution_receipts_v2(self, *, query: Optional[ListExecutionReceiptsV2Query] = None) -> ListExecutionReceiptsV2Result:
        """List canonical inclusion, finality, reconciliation, and attribution receipts"""
        return cast(ListExecutionReceiptsV2Result, self._request("GET", "/receipts", query=query, accept="application/json"))

    def get_execution_receipt_v2(self, *, path: GetExecutionReceiptV2Path) -> GetExecutionReceiptV2Result:
        """Read one canonical execution receipt projection"""
        return cast(GetExecutionReceiptV2Result, self._request("GET", "/receipts/{id}", path=path, accept="application/json"))

    def list_alerts_v2(self, *, query: Optional[ListAlertsV2Query] = None) -> ListAlertsV2Result:
        """List typed anomaly alerts with immutable evidence"""
        return cast(ListAlertsV2Result, self._request("GET", "/alerts", query=query, accept="application/json"))

    def list_proof_v2(self, *, query: Optional[ListProofV2Query] = None) -> ListProofV2Result:
        """List signed passports and content-addressed proof artifacts"""
        return cast(ListProofV2Result, self._request("GET", "/proof", query=query, accept="application/json"))

    def list_operating_system_providers(self) -> ListOperatingSystemProvidersResult:
        """List tenant-scoped signed provider registrations and health"""
        return cast(ListOperatingSystemProvidersResult, self._request("GET", "/providers", accept="application/json"))

    def put_operating_system_provider(self, *, body: PutOperatingSystemProviderBody, idempotency_key: str, if_match: Optional[str] = None) -> PutOperatingSystemProviderResult:
        """Register or rotate an attested provider generation"""
        return cast(PutOperatingSystemProviderResult, self._request("POST", "/providers", body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_operating_system_artifacts(self, *, query: Optional[ListOperatingSystemArtifactsQuery] = None) -> ListOperatingSystemArtifactsResult:
        """List immutable object-storage lineage for reports and large evidence"""
        return cast(ListOperatingSystemArtifactsResult, self._request("GET", "/artifacts", query=query, accept="application/json"))

    def get_treasury_summary(self) -> GetTreasurySummaryResult:
        """Get reconciled treasury ledger summary"""
        return cast(GetTreasurySummaryResult, self._request("GET", "/treasury/summary", accept="application/json"))

    def get_unified_liquidity_map(self) -> GetUnifiedLiquidityMapResult:
        """Get the unified read-only/write-authority-aware venue map"""
        return cast(GetUnifiedLiquidityMapResult, self._request("GET", "/market-map", accept="application/json"))

    def run_non_custodial_sandbox_study(self, *, body: RunNonCustodialSandboxStudyBody, idempotency_key: str) -> RunNonCustodialSandboxStudyResult:
        """Persist a deterministic non-custodial study with no execution authority"""
        return cast(RunNonCustodialSandboxStudyResult, self._request("POST", "/sandbox/studies", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def create_study_share_link(self, *, path: CreateStudyShareLinkPath, body: CreateStudyShareLinkBody, idempotency_key: str) -> CreateStudyShareLinkResult:
        """Create a private expiring or issuer-approved public study link"""
        return cast(CreateStudyShareLinkResult, self._request("POST", "/studies/{id}/share-links", path=path, body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def revoke_study_share_link(self, *, path: RevokeStudyShareLinkPath, body: RevokeStudyShareLinkBody, idempotency_key: str, if_match: str) -> RevokeStudyShareLinkResult:
        """Immediately revoke a private or public study share without deleting evidence"""
        return cast(RevokeStudyShareLinkResult, self._request("POST", "/study-shares/{id}/revoke", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def revoke_liquidity_passport(self, *, path: RevokeLiquidityPassportPath, body: RevokeLiquidityPassportBody, idempotency_key: str, if_match: str) -> RevokeLiquidityPassportResult:
        """Immediately revoke a published passport without deleting signed evidence"""
        return cast(RevokeLiquidityPassportResult, self._request("POST", "/passports/{id}/revoke", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def create_signed_study_report(self, *, path: CreateSignedStudyReportPath, body: CreateSignedStudyReportBody, idempotency_key: str) -> CreateSignedStudyReportResult:
        """Queue a signed JSON, PDF, and CSV report"""
        return cast(CreateSignedStudyReportResult, self._request("POST", "/studies/{id}/reports", path=path, body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_study_report_jobs(self, *, path: ListStudyReportJobsPath) -> ListStudyReportJobsResult:
        """List report job state and dead-letter evidence"""
        return cast(ListStudyReportJobsResult, self._request("GET", "/studies/{id}/report-jobs", path=path, accept="application/json"))

    def wrap_legacy_strategy_definition(self, *, body: WrapLegacyStrategyDefinitionBody, idempotency_key: str) -> WrapLegacyStrategyDefinitionResult:
        """Wrap immutable v1 Bootstrap, Maintain, or Diversify evidence in the declarative v2 schema"""
        return cast(WrapLegacyStrategyDefinitionResult, self._request("POST", "/strategies/legacy-wrappers", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def admit_strategy_proposal(self, *, path: AdmitStrategyProposalPath, body: AdmitStrategyProposalBody, idempotency_key: str, if_match: str) -> AdmitStrategyProposalResult:
        """Derive all eight proposal-admission checks from immutable server-side evidence"""
        return cast(AdmitStrategyProposalResult, self._request("POST", "/strategies/{id}/proposal-admissions", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_strategy_evidence(self, *, path: GetStrategyEvidencePath, query: GetStrategyEvidenceQuery) -> GetStrategyEvidenceResult:
        """Read exact strategy admission events and their immutable study generations"""
        return cast(GetStrategyEvidenceResult, self._request("GET", "/strategies/{id}/evidence", path=path, query=query, accept="application/json"))

    def get_incentive_evidence(self, *, path: GetIncentiveEvidencePath, query: GetIncentiveEvidenceQuery) -> GetIncentiveEvidenceResult:
        """Read optimization and preparation events bound to an exact incentive program generation"""
        return cast(GetIncentiveEvidenceResult, self._request("GET", "/incentive-programs/{id}/evidence", path=path, query=query, accept="application/json"))

    def approve_strategy_package(self, *, path: ApproveStrategyPackagePath, body: ApproveStrategyPackageBody, idempotency_key: str, if_match: str) -> ApproveStrategyPackageResult:
        """Verify independent named reviews and a current signed strategy-registry generation"""
        return cast(ApproveStrategyPackageResult, self._request("POST", "/strategy-packages/{id}/approve", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def seed_strategy_from_approved_package(self, *, path: SeedStrategyFromApprovedPackagePath, body: SeedStrategyFromApprovedPackageBody, idempotency_key: str, if_match: str) -> SeedStrategyFromApprovedPackageResult:
        """Enter standard activation preparation only from a currently verifiable approved package"""
        return cast(SeedStrategyFromApprovedPackageResult, self._request("POST", "/strategy-packages/{id}/seed-strategy", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def revoke_strategy_package(self, *, path: RevokeStrategyPackagePath, body: RevokeStrategyPackageBody, idempotency_key: str, if_match: str) -> RevokeStrategyPackageResult:
        """Immediately revoke activation eligibility while retaining evidence"""
        return cast(RevokeStrategyPackageResult, self._request("POST", "/strategy-packages/{id}/revoke", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_proposal_comments(self, *, path: ListProposalCommentsPath) -> ListProposalCommentsResult:
        """listProposalComments"""
        return cast(ListProposalCommentsResult, self._request("GET", "/proposals/{id}/comments", path=path, accept="application/json"))

    def append_proposal_comment(self, *, path: AppendProposalCommentPath, body: AppendProposalCommentBody, idempotency_key: str, if_match: str) -> AppendProposalCommentResult:
        """appendProposalComment"""
        return cast(AppendProposalCommentResult, self._request("POST", "/proposals/{id}/comments", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def decide_proposal(self, *, path: DecideProposalPath, body: DecideProposalBody, idempotency_key: str, if_match: str) -> DecideProposalResult:
        """Append an internal approval or rejection to a current DRAFT/VALIDATED packet"""
        return cast(DecideProposalResult, self._request("POST", "/proposals/{id}/decisions", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def register_proposal_safe_submission(self, *, path: RegisterProposalSafeSubmissionPath, body: RegisterProposalSafeSubmissionBody, idempotency_key: str, if_match: str) -> RegisterProposalSafeSubmissionResult:
        """Resolve finalized/reconciled issuer-Safe evidence server-side for an exact typed controller action"""
        return cast(RegisterProposalSafeSubmissionResult, self._request("POST", "/proposals/{id}/safe-submissions", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def compare_proposals(self, *, body: CompareProposalsBody, idempotency_key: str) -> CompareProposalsResult:
        """Build an immutable comparison hash for two to eight decision packets"""
        return cast(CompareProposalsResult, self._request("POST", "/proposal-comparisons", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def append_launch_timeline_event(self, *, path: AppendLaunchTimelineEventPath, body: AppendLaunchTimelineEventBody, idempotency_key: str, if_match: str) -> AppendLaunchTimelineEventResult:
        """Append a PLANNED dependency-aware event; completion is available only through the approval route"""
        return cast(AppendLaunchTimelineEventResult, self._request("POST", "/launch-plans/{id}/timeline-events", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_launch_timeline(self, *, path: GetLaunchTimelinePath) -> GetLaunchTimelineResult:
        """Materialize dependency and completion state from immutable events"""
        return cast(GetLaunchTimelineResult, self._request("GET", "/launch-plans/{id}/timeline", path=path, accept="application/json"))

    def complete_launch_timeline_event(self, *, path: CompleteLaunchTimelineEventPath, body: CompleteLaunchTimelineEventBody, idempotency_key: str, if_match: str) -> CompleteLaunchTimelineEventResult:
        """Bind a completion receipt after every dependency completes"""
        return cast(CompleteLaunchTimelineEventResult, self._request("POST", "/launch-plans/{id}/timeline-events/{eventId}/complete", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def seed_launch_workspace(self, *, path: SeedLaunchWorkspacePath, body: SeedLaunchWorkspaceBody, idempotency_key: str, if_match: str) -> SeedLaunchWorkspaceResult:
        """Seed drafts, studies, policy, qualification, and a funding proposal without execution"""
        return cast(SeedLaunchWorkspaceResult, self._request("POST", "/launch-plans/{id}/seed-workspace", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def seed_issuer_intent_from_capital_study(self, *, path: SeedIssuerIntentFromCapitalStudyPath, body: SeedIssuerIntentFromCapitalStudyBody, idempotency_key: str, if_match: Optional[str] = None) -> SeedIssuerIntentFromCapitalStudyResult:
        """Create or append an issuer-intent version from a completed reproducible capital study"""
        return cast(SeedIssuerIntentFromCapitalStudyResult, self._request("POST", "/capital-requirements/{id}/seed-intent", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def seed_launch_plan_from_capital_study(self, *, path: SeedLaunchPlanFromCapitalStudyPath, body: SeedLaunchPlanFromCapitalStudyBody, idempotency_key: str, if_match: Optional[str] = None) -> SeedLaunchPlanFromCapitalStudyResult:
        """Create or append a launch-plan draft using deterministic capital-study outputs"""
        return cast(SeedLaunchPlanFromCapitalStudyResult, self._request("POST", "/capital-requirements/{id}/seed-launch-plan", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def reserve_treasury_from_capital_study(self, *, path: ReserveTreasuryFromCapitalStudyPath, body: ReserveTreasuryFromCapitalStudyBody, idempotency_key: str) -> ReserveTreasuryFromCapitalStudyResult:
        """Append a signed offchain treasury reservation without moving funds"""
        return cast(ReserveTreasuryFromCapitalStudyResult, self._request("POST", "/capital-requirements/{id}/reservations", path=path, body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def queue_venue_index(self, *, path: QueueVenueIndexPath, body: QueueVenueIndexBody, idempotency_key: str) -> QueueVenueIndexResult:
        """Queue signed RPC quorum and finality indexing for one exact current venue-profile generation"""
        return cast(QueueVenueIndexResult, self._request("POST", "/venues/{id}/index-jobs", path=path, body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_migration_plan_state(self, *, path: GetMigrationPlanStatePath) -> GetMigrationPlanStateResult:
        """Materialize ordered forward and rollback state from immutable transition evidence"""
        return cast(GetMigrationPlanStateResult, self._request("GET", "/migration-plans/{id}/state", path=path, accept="application/json"))

    def append_migration_plan_transition(self, *, path: AppendMigrationPlanTransitionPath, body: AppendMigrationPlanTransitionBody, idempotency_key: str, if_match: str) -> AppendMigrationPlanTransitionResult:
        """Request a server-verified action-specific migration lifecycle transition"""
        return cast(AppendMigrationPlanTransitionResult, self._request("POST", "/migration-plans/{id}/transitions", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def compile_policy_intent(self, *, path: CompilePolicyIntentPath, body: CompilePolicyIntentBody, idempotency_key: str, if_match: str) -> CompilePolicyIntentResult:
        """Deterministically compile a non-executable policy draft"""
        return cast(CompilePolicyIntentResult, self._request("POST", "/policy-intent-drafts/{id}/compile", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def create_structured_policy_intent_draft(self, *, body: CreateStructuredPolicyIntentDraftBody, idempotency_key: str) -> CreateStructuredPolicyIntentDraftResult:
        """Create a deterministic typed policy draft without an AI provider"""
        return cast(CreateStructuredPolicyIntentDraftResult, self._request("POST", "/policy-intent-drafts/structured", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def check_autonomy_policy(self, *, body: CheckAutonomyPolicyBody, idempotency_key: str) -> CheckAutonomyPolicyResult:
        """Validate a manually structured policy and persist non-executable evidence"""
        return cast(CheckAutonomyPolicyResult, self._request("POST", "/policy-checks", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def rotate_developer_credential(self, *, path: RotateDeveloperCredentialPath, body: RotateDeveloperCredentialBody, idempotency_key: str, if_match: str) -> RotateDeveloperCredentialResult:
        """Rotate a hashed API key or OAuth client secret"""
        return cast(RotateDeveloperCredentialResult, self._request("POST", "/developer-credentials/{id}/rotate", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_partner_portfolio(self, *, path: GetPartnerPortfolioPath) -> GetPartnerPortfolioResult:
        """Read issuer aggregates only where bilateral partner consent is active"""
        return cast(GetPartnerPortfolioResult, self._request("GET", "/partner-portfolios/{partnerId}", path=path, accept="application/json"))

    def get_partner_consent_options(self, *, query: GetPartnerConsentOptionsQuery) -> GetPartnerConsentOptionsResult:
        """Review the current partner declarations for this explicitly assigned issuer"""
        return cast(GetPartnerConsentOptionsResult, self._request("GET", "/partner-consent-options", query=query, accept="application/json"))

    def get_partner_preparation_context(self, *, path: GetPartnerPreparationContextPath, query: GetPartnerPreparationContextQuery) -> GetPartnerPreparationContextResult:
        """Read the exact current actor-scoped consent for preparing an issuer packet"""
        return cast(GetPartnerPreparationContextResult, self._request("GET", "/partner-preparation-contexts/{partnerId}", path=path, query=query, accept="application/json"))

    def get_partner_preparation_receipt_recovery(self, *, path: GetPartnerPreparationReceiptRecoveryPath, query: GetPartnerPreparationReceiptRecoveryQuery, idempotency_key: str) -> GetPartnerPreparationReceiptRecoveryResult:
        """Recover the initiating partner actor's durable preparation receipt using its original operation key"""
        return cast(GetPartnerPreparationReceiptRecoveryResult, self._request("GET", "/partner-preparation-receipts/{partnerId}", path=path, query=query, idempotency_key=idempotency_key, accept="application/json"))

    def list_partner_preparations(self) -> ListPartnerPreparationsResult:
        """Read consent-bound partner packets awaiting or completed in issuer review"""
        return cast(ListPartnerPreparationsResult, self._request("GET", "/partner-preparations", accept="application/json"))

    def import_partner_preparation(self, *, path: ImportPartnerPreparationPath, body: ImportPartnerPreparationBody, idempotency_key: str, if_match: str) -> ImportPartnerPreparationResult:
        """Import a current consent-bound partner packet as an approval-empty issuer proposal"""
        return cast(ImportPartnerPreparationResult, self._request("POST", "/partner-preparations/{eventId}/import", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def decline_partner_preparation(self, *, path: DeclinePartnerPreparationPath, body: DeclinePartnerPreparationBody, idempotency_key: str, if_match: str) -> DeclinePartnerPreparationResult:
        """Record an issuer decline of an exact current consent-bound partner packet"""
        return cast(DeclinePartnerPreparationResult, self._request("POST", "/partner-preparations/{eventId}/decline", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_partner_preparation_status(self, *, path: GetPartnerPreparationStatusPath, query: GetPartnerPreparationStatusQuery) -> GetPartnerPreparationStatusResult:
        """Read partner-owned delivery and issuer review status for one exact packet"""
        return cast(GetPartnerPreparationStatusResult, self._request("GET", "/partner-preparation-status/{partnerId}/{eventId}", path=path, query=query, accept="application/json"))

    def list_partner_domain_challenges(self, *, query: Optional[ListPartnerDomainChallengesQuery] = None) -> ListPartnerDomainChallengesResult:
        """List tenant-owned domain ownership and HTTPS onboarding challenges"""
        return cast(ListPartnerDomainChallengesResult, self._request("GET", "/partner-domain-challenges", query=query, accept="application/json"))

    def create_partner_domain_challenge(self, *, body: CreatePartnerDomainChallengeBody, idempotency_key: str) -> CreatePartnerDomainChallengeResult:
        """Create an exact-host DNS ownership challenge for an approved domain verifier"""
        return cast(CreatePartnerDomainChallengeResult, self._request("POST", "/partner-domain-challenges", body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_partner_domain_challenge(self, *, path: GetPartnerDomainChallengePath) -> GetPartnerDomainChallengeResult:
        """Read one tenant-owned domain onboarding challenge"""
        return cast(GetPartnerDomainChallengeResult, self._request("GET", "/partner-domain-challenges/{id}", path=path, accept="application/json"))

    def get_partner_domain_status(self, *, path: GetPartnerDomainStatusPath) -> GetPartnerDomainStatusResult:
        """Check current DNS ownership, routing and HTTPS readiness"""
        return cast(GetPartnerDomainStatusResult, self._request("GET", "/partner-domain-challenges/{id}/status", path=path, accept="application/json"))

    def verify_partner_domain_challenge(self, *, path: VerifyPartnerDomainChallengePath, body: VerifyPartnerDomainChallengeBody, idempotency_key: str) -> VerifyPartnerDomainChallengeResult:
        """Verify the exact DNS TXT response and obtain current signed domain evidence"""
        return cast(VerifyPartnerDomainChallengeResult, self._request("POST", "/partner-domain-challenges/{id}/verify", path=path, body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def provision_partner_domain_challenge(self, *, path: ProvisionPartnerDomainChallengePath, body: ProvisionPartnerDomainChallengeBody, idempotency_key: str) -> ProvisionPartnerDomainChallengeResult:
        """Provision a verified partner hostname through the configured HTTPS provider"""
        return cast(ProvisionPartnerDomainChallengeResult, self._request("POST", "/partner-domain-challenges/{id}/provision", path=path, body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def revoke_partner_domain_challenge(self, *, path: RevokePartnerDomainChallengePath, body: RevokePartnerDomainChallengeBody, idempotency_key: str) -> RevokePartnerDomainChallengeResult:
        """Revoke an unbound domain challenge and remove its managed hostname"""
        return cast(RevokePartnerDomainChallengeResult, self._request("POST", "/partner-domain-challenges/{id}/revoke", path=path, body=body, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def prepare_partner_proposal(self, *, path: PreparePartnerProposalPath, body: PreparePartnerProposalBody, idempotency_key: str, if_match: str) -> PreparePartnerProposalResult:
        """Prepare an issuer import packet through exact current bilateral consent without cross-tenant or Safe authority"""
        return cast(PreparePartnerProposalResult, self._request("POST", "/partner-portfolios/{partnerId}/proposal-preparations", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def revoke_partner_tenant(self, *, path: RevokePartnerTenantPath, body: RevokePartnerTenantBody, idempotency_key: str, if_match: str) -> RevokePartnerTenantResult:
        """Immediately remove all host bindings for a partner configuration"""
        return cast(RevokePartnerTenantResult, self._request("POST", "/partners/{id}/revoke", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_partner_consents(self) -> ListPartnerConsentsResult:
        """List the issuer tenant’s current bilateral consent records"""
        return cast(ListPartnerConsentsResult, self._request("GET", "/partner-consents", accept="application/json"))

    def grant_partner_consent(self, *, body: GrantPartnerConsentBody, idempotency_key: str, if_match: Optional[str] = None) -> GrantPartnerConsentResult:
        """Grant or regrant explicit actor-scoped bilateral access"""
        return cast(GrantPartnerConsentResult, self._request("POST", "/partner-consents", body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def get_partner_consent(self, *, path: GetPartnerConsentPath) -> GetPartnerConsentResult:
        """Read one issuer-owned partner consent"""
        return cast(GetPartnerConsentResult, self._request("GET", "/partner-consents/{id}", path=path, accept="application/json"))

    def revoke_partner_consent(self, *, path: RevokePartnerConsentPath, body: RevokePartnerConsentBody, idempotency_key: str, if_match: str) -> RevokePartnerConsentResult:
        """Immediately revoke portfolio and proposal-preparation access"""
        return cast(RevokePartnerConsentResult, self._request("POST", "/partner-consents/{id}/revoke", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_market_maker_evidence(self, *, path: ListMarketMakerEvidencePath) -> ListMarketMakerEvidenceResult:
        """List provenance-preserving market-maker observations and reconciliation state"""
        return cast(ListMarketMakerEvidenceResult, self._request("GET", "/market-maker-mandates/{id}/observations", path=path, accept="application/json"))

    def ingest_market_maker_evidence(self, *, path: IngestMarketMakerEvidencePath, body: IngestMarketMakerEvidenceBody, idempotency_key: str, if_match: str) -> IngestMarketMakerEvidenceResult:
        """Ingest a finalized onchain or signed API/file/exchange observation without custody authority"""
        return cast(IngestMarketMakerEvidenceResult, self._request("POST", "/market-maker-mandates/{id}/observations", path=path, body=body, if_match=if_match, idempotency_key=idempotency_key, content_type="application/json", accept="application/json"))

    def list_operating_system_jobs(self) -> ListOperatingSystemJobsResult:
        """List fenced worker jobs and dead-letter visibility"""
        return cast(ListOperatingSystemJobsResult, self._request("GET", "/jobs", accept="application/json"))

    def get_public_liquidity_passport(self, *, path: GetPublicLiquidityPassportPath) -> GetPublicLiquidityPassportResult:
        """Verify an issuer-disclosed signed Liquidity Passport"""
        return cast(GetPublicLiquidityPassportResult, self._request("GET", "/public/passports/{slug}", path=path, accept="application/json"))

    def download_public_liquidity_passport(self, *, path: DownloadPublicLiquidityPassportPath) -> DownloadPublicLiquidityPassportResult:
        """Download deterministic signed JSON, HTML, PDF, or CSV"""
        return cast(DownloadPublicLiquidityPassportResult, self._request("GET", "/public/passports/{slug}/formats/{format}", path=path, accept="application/json, text/html, application/pdf, text/csv"))

    def download_liquidity_passport_verification_bundle(self, *, path: DownloadLiquidityPassportVerificationBundlePath) -> DownloadLiquidityPassportVerificationBundleResult:
        """Download canonical passport, trust anchor, artifact hashes, and registry commitment"""
        return cast(DownloadLiquidityPassportVerificationBundleResult, self._request("GET", "/public/passports/{slug}/verification-bundle", path=path, accept="application/json"))

    def get_shared_simulation_study(self, *, path: GetSharedSimulationStudyPath) -> GetSharedSimulationStudyResult:
        """Read a non-revoked study share"""
        return cast(GetSharedSimulationStudyResult, self._request("GET", "/public/studies/{slug}", path=path, accept="application/json"))

    def get_verified_host_brand(self) -> GetVerifiedHostBrandResult:
        """Resolve a privacy-safe brand only for the exact verified request host"""
        return cast(GetVerifiedHostBrandResult, self._request("GET", "/public/brands/current", accept="application/json"))

    def get_verified_partner_brand_logo(self, *, path: GetVerifiedPartnerBrandLogoPath) -> GetVerifiedPartnerBrandLogoResult:
        """Serve the exact current host-bound content-addressed PNG logo"""
        return cast(GetVerifiedPartnerBrandLogoResult, self._request("GET", "/public/partner-brand/logo/{contentHash}", path=path, accept="image/png"))

    def oauth_client_credentials(self, client_id: str, client_secret: str, scopes: tuple[str, ...] = ()) -> IssueOperatingSystemOAuthTokenResult:
        body: IssueOperatingSystemOAuthTokenBody = {"grant_type": "client_credentials"}
        if scopes:
            body["scope"] = " ".join(scopes)
        return self.issue_operating_system_oauth_token(body=body, client_id=client_id, client_secret=client_secret)
