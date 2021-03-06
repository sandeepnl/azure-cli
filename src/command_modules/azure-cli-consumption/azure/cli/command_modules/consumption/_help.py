# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.help_files import helps

helps['consumption'] = """
    type: group
    short-summary: View consumption of Azure resources.
"""

helps['consumption usage list'] = """
    type: command
    short-summary: Shows the usage details of Azure resource consumption, either by biling period or within a specific date range.
"""
