# Action Plan

## 24 hours (Quick wins)
- Disable router HTTP; enforce HTTPS only
- Confirm remote management is off for WAN
- Rotate admin credentials (router + IoT)

## 7 days
- Update router and IoT firmware
- Export/backup router configuration
- Document basic topology

## 30 days
- Segment IoT (guest network / VLAN)
- Deploy Wazuh + Suricata
- Tune baseline alerts (new device, DNS anomalies, brute force, suspicious outbound)
