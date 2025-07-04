# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T14:54:51+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity

from models import (
    AcademicCertificateSchema,
    HpcerCertificatePostRequest,
    HpcerCertificatePostResponse,
    HpcerCertificatePostResponse1,
    HpcerCertificatePostResponse2,
    HpcerCertificatePostResponse3,
    HpcerCertificatePostResponse4,
    HpcerCertificatePostResponse5,
    HpcerCertificatePostResponse6,
    HscerCertificatePostRequest,
    HscerCertificatePostResponse,
    HscerCertificatePostResponse1,
    HscerCertificatePostResponse2,
    HscerCertificatePostResponse3,
    HscerCertificatePostResponse4,
    HscerCertificatePostResponse5,
    HscerCertificatePostResponse6,
    HsmgrCertificatePostRequest,
    HsmgrCertificatePostResponse,
    HsmgrCertificatePostResponse1,
    HsmgrCertificatePostResponse2,
    HsmgrCertificatePostResponse3,
    HsmgrCertificatePostResponse4,
    HsmgrCertificatePostResponse5,
    HsmgrCertificatePostResponse6,
    NchscCertificatePostRequest,
    NchscCertificatePostResponse,
    NchscCertificatePostResponse1,
    NchscCertificatePostResponse2,
    NchscCertificatePostResponse3,
    NchscCertificatePostResponse4,
    NchscCertificatePostResponse5,
    NchscCertificatePostResponse6,
    NctscCertificatePostRequest,
    NctscCertificatePostResponse,
    NctscCertificatePostResponse1,
    NctscCertificatePostResponse2,
    NctscCertificatePostResponse3,
    NctscCertificatePostResponse4,
    NctscCertificatePostResponse5,
    NctscCertificatePostResponse6,
    NsescCertificatePostRequest,
    NsescCertificatePostResponse,
    NsescCertificatePostResponse1,
    NsescCertificatePostResponse2,
    NsescCertificatePostResponse3,
    NsescCertificatePostResponse4,
    NsescCertificatePostResponse5,
    NsescCertificatePostResponse6,
    NstscCertificatePostRequest,
    NstscCertificatePostResponse,
    NstscCertificatePostResponse1,
    NstscCertificatePostResponse2,
    NstscCertificatePostResponse3,
    NstscCertificatePostResponse4,
    NstscCertificatePostResponse5,
    NstscCertificatePostResponse6,
    NtltrCertificatePostRequest,
    NtltrCertificatePostResponse,
    NtltrCertificatePostResponse1,
    NtltrCertificatePostResponse2,
    NtltrCertificatePostResponse3,
    NtltrCertificatePostResponse4,
    NtltrCertificatePostResponse5,
    NtltrCertificatePostResponse6,
    NtmksCertificatePostRequest,
    NtmksCertificatePostResponse,
    NtmksCertificatePostResponse1,
    NtmksCertificatePostResponse2,
    NtmksCertificatePostResponse3,
    NtmksCertificatePostResponse4,
    NtmksCertificatePostResponse5,
    NtmksCertificatePostResponse6,
    SkhscCertificatePostRequest,
    SkhscCertificatePostResponse,
    SkhscCertificatePostResponse1,
    SkhscCertificatePostResponse2,
    SkhscCertificatePostResponse3,
    SkhscCertificatePostResponse4,
    SkhscCertificatePostResponse5,
    SkhscCertificatePostResponse6,
    SktscCertificatePostRequest,
    SktscCertificatePostResponse,
    SktscCertificatePostResponse1,
    SktscCertificatePostResponse2,
    SktscCertificatePostResponse3,
    SktscCertificatePostResponse4,
    SktscCertificatePostResponse5,
    SktscCertificatePostResponse6,
    SpcerCertificatePostRequest,
    SpcerCertificatePostResponse,
    SpcerCertificatePostResponse1,
    SpcerCertificatePostResponse2,
    SpcerCertificatePostResponse3,
    SpcerCertificatePostResponse4,
    SpcerCertificatePostResponse5,
    SpcerCertificatePostResponse6,
    SscerCertificatePostRequest,
    SscerCertificatePostResponse,
    SscerCertificatePostResponse1,
    SscerCertificatePostResponse2,
    SscerCertificatePostResponse3,
    SscerCertificatePostResponse4,
    SscerCertificatePostResponse5,
    SscerCertificatePostResponse6,
    SsmgrCertificatePostRequest,
    SsmgrCertificatePostResponse,
    SsmgrCertificatePostResponse1,
    SsmgrCertificatePostResponse2,
    SsmgrCertificatePostResponse3,
    SsmgrCertificatePostResponse4,
    SsmgrCertificatePostResponse5,
    SsmgrCertificatePostResponse6,
    TetcrCertificatePostRequest,
    TetcrCertificatePostResponse,
    TetcrCertificatePostResponse1,
    TetcrCertificatePostResponse2,
    TetcrCertificatePostResponse3,
    TetcrCertificatePostResponse4,
    TetcrCertificatePostResponse5,
    TetcrCertificatePostResponse6,
    TetmsCertificatePostRequest,
    TetmsCertificatePostResponse,
    TetmsCertificatePostResponse1,
    TetmsCertificatePostResponse2,
    TetmsCertificatePostResponse3,
    TetmsCertificatePostResponse4,
    TetmsCertificatePostResponse5,
    TetmsCertificatePostResponse6,
)

app = MCPProxy(
    description='CBSE (http://www.cbse.nic.in/) is issuing marksheets, passing certificates, migration certificates etc. through DigiLocker. These are either pushed, or can be pulled by students into their DigiLocker accounts. Currently available - 2004 - 2020 [Class XII], 2004 - 2020 [Class X], 2017 (NEET Rank Letter & Marksheet), 2016 (NEET Rank Letter), 2018 December (CTET Eligibility Certificate & Marksheet).',
    termsOfService='https://apisetu.gov.in/terms.php',
    title='Central Board of Secondary Education',
    version='3.0.0',
    servers=[{'url': 'https://apisetu.gov.in/cbse/v3'}],
)


@app.post(
    '/hpcer/certificate',
    description=""" API to verify Class XII Passing Certificate. """,
    tags=['certificate_generation'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def hpcer(body: HpcerCertificatePostRequest = None):
    """
    Class XII Passing Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/hscer/certificate',
    description=""" API to verify Class XII Marksheet. """,
    tags=['certificate_generation'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def hscer(body: HscerCertificatePostRequest = None):
    """
    Class XII Marksheet
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/hsmgr/certificate',
    description=""" API to verify Class XII Migration Certificate. """,
    tags=['certificate_generation'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def hsmgr(body: HsmgrCertificatePostRequest = None):
    """
    Class XII Migration Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/nchsc/certificate',
    description=""" API to verify NCHMCT Skill Certificate (X). """,
    tags=['certificate_generation', 'skill_certificate_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def nchsc(body: NchscCertificatePostRequest = None):
    """
    NCHMCT Skill Certificate (X)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/nctsc/certificate',
    description=""" API to verify NCHMCT Skill Certificate (XII). """,
    tags=['certificate_generation', 'skill_certificate_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def nctsc(body: NctscCertificatePostRequest = None):
    """
    NCHMCT Skill Certificate (XII)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/nsesc/certificate',
    description=""" API to verify NSE Skill Certificate (X). """,
    tags=['certificate_generation', 'skill_certificate_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def nsesc(body: NsescCertificatePostRequest = None):
    """
    NSE Skill Certificate (X)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/nstsc/certificate',
    description=""" API to verify NSE Skill Certificate (XII). """,
    tags=['skill_certificate_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def nstsc(body: NstscCertificatePostRequest = None):
    """
    NSE Skill Certificate (XII)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/ntltr/certificate',
    description=""" API to verify NEET Rank Letter. """,
    tags=['neet_certificate_processing'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def ntltr(body: NtltrCertificatePostRequest = None):
    """
    NEET Rank Letter
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/ntmks/certificate',
    description=""" API to verify NEET Marksheet. """,
    tags=['neet_certificate_processing', 'certificate_generation'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def ntmks(body: NtmksCertificatePostRequest = None):
    """
    NEET Marksheet
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/skhsc/certificate',
    description=""" API to verify Skill Certificate (X). """,
    tags=['skill_certificate_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def skhsc(body: SkhscCertificatePostRequest = None):
    """
    Skill Certificate (X)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/sktsc/certificate',
    description=""" API to verify Skill Certificate (XII). """,
    tags=['certificate_generation', 'skill_certificate_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def sktsc(body: SktscCertificatePostRequest = None):
    """
    Skill Certificate (XII)
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/spcer/certificate',
    description=""" API to verify Class X Passing Certificate. """,
    tags=['certificate_generation'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def spcer(body: SpcerCertificatePostRequest = None):
    """
    Class X Passing Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/sscer/certificate',
    description=""" API to verify Class X Marksheet. """,
    tags=['certificate_generation', 'teachers_eligibility_certificates'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def sscer(body: SscerCertificatePostRequest = None):
    """
    Class X Marksheet
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/ssmgr/certificate',
    description=""" API to verify Class X Migration Certificate. """,
    tags=['certificate_generation'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def ssmgr(body: SsmgrCertificatePostRequest = None):
    """
    Class X Migration Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/tetcr/certificate',
    description=""" API to verify Teachers Eligibility Test Certificate. """,
    tags=['teachers_eligibility_certificates', 'certificate_generation'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def tetcr(body: TetcrCertificatePostRequest = None):
    """
    Teachers Eligibility Test Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/tetms/certificate',
    description=""" API to verify Teachers Eligibility Test Mark Sheet. """,
    tags=['certificate_generation', 'teachers_eligibility_certificates'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def tetms(body: TetmsCertificatePostRequest = None):
    """
    Teachers Eligibility Test Mark Sheet
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
