 # Import dnspython resolver to fetch DNS records
import dns.resolver

# Define function to run DNS analysis for a domain
def run_dns_analysis(domain: str) -> str:
    try:
        # Initialize result list to store DNS records
        result = []
        # Loop through desired DNS record types
        for record_type in ["A", "AAAA", "MX", "NS", "SOA"]:
            # Resolve DNS records for the domain
            answers = dns.resolver.resolve(domain, record_type, raise_on_no_answer=False)
            # Add record type header to result
            result.append(f"{record_type} records:")
            # Append each record to result list
            for rdata in answers:
                result.append(str(rdata))
        # Return formatted result as string
        return "\n".join(result)
    except Exception as e:
        # Return error message if DNS resolution fails
        return f"DNS analysis failed: {str(e)}"