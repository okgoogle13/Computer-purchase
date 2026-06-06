/**
 * agent_browser_spec_gapfill.js — Scaffold importer logic.
 * Extract specs including battery fields from listing detail text.
 */

/**
 * Extracts battery specifications from listing title and description.
 * @param {string} title - The title of the listing.
 * @param {string} description - The description or details of the listing.
 * @returns {object} Extracted battery fields.
 */
function extractBatterySpecs(title, description) {
    const text = ((title || '') + ' ' + (description || '')).toLowerCase();
    
    let battery_replaced = false;
    let battery_disclosure_level = 'none';
    let battery_health_pct = null;
    let battery_cycle_count = null;

    // Check for replaced / new battery
    if (text.includes('battery replaced') || text.includes('new battery')) {
        battery_replaced = true;
        battery_disclosure_level = 'replaced';
    }

    // Check for health pct: e.g. "90% battery", "battery 95% health"
    // Regex matches e.g. 90% battery or battery 95%
    const pctMatch = text.match(/(\d{2,3})%.*?batter/i) || text.match(/batter.*?(\d{2,3})%/i);
    if (pctMatch) {
        const pctVal = parseInt(pctMatch[1], 10);
        if (pctVal >= 0 && pctVal <= 100) {
            battery_health_pct = pctVal;
            if (battery_disclosure_level !== 'replaced') {
                battery_disclosure_level = 'tested_pct';
            }
        }
    }

    // Check for cycles: e.g. "cycle count 120", "cycles: 45"
    const cycleMatch = text.match(/cycle\s*count\s*(\d{1,4})/i) || text.match(/cycle.*?(\d{1,4})/i);
    if (cycleMatch) {
        battery_cycle_count = parseInt(cycleMatch[1], 10);
        if (battery_disclosure_level === 'tested_pct') {
            battery_disclosure_level = 'tested_pct_cycles';
        }
    }

    // Check for range claim: e.g. "battery 80-89% health"
    if (battery_disclosure_level === 'none') {
        const rangeMatch = text.match(/batter.*\b(\d{2}-\d{2})%/i) || text.match(/\b(\d{2}-\d{2})%.*?batter/i);
        if (rangeMatch) {
            battery_disclosure_level = 'health_range_claim';
        }
    }

    // Check for sold as is
    if (battery_disclosure_level === 'none') {
        if (/as\s*is|not\s*tested/.test(text)) {
            battery_disclosure_level = 'sold_as_is';
        }
    }

    // Check for vague claim
    if (battery_disclosure_level === 'none') {
        if (text.includes('holds charge') || text.includes('good batt')) {
            battery_disclosure_level = 'vague_claim';
        }
    }

    return {
        battery_disclosure_level,
        battery_health_pct,
        battery_cycle_count,
        battery_replaced
    };
}

module.exports = {
    extractBatterySpecs
};
