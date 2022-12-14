"""Bash scripts for manual parsing in terminal"""

PS_AUX = "ps aux"
UNIQ_USERS = """ awk 'NR>1{tot[$1]++;} END{for(id in tot) printf "%s, ", id}'"""
COUNT_PROC = " awk '{print $2}' | wc -l"
EACH_USER_PROC = """awk 'NR>1{tot[$1]++;} END{for(id in tot) printf "%s = %s, ", id, tot[id]}'"""
MEMORY_USAGE = "awk '{sum +=$4}; END {print sum}' | grep -v %MEM"
CPU_USAGE = "awk '{sum +=$3}; END {print sum}'"
MAX_MEM = "--sort -%mem  | awk '{print $4, $11}'"
MAX_CPU = "--sort -%cpu  | awk '{print $3, $11}'"


