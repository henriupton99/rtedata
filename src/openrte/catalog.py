from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Catalog:
    _structure: Dict[str, list[str]] = field(init=False, repr=False)

    def __post_init__(self):
      self.request_base_url = "https://digital.iservices.rte-france.com/open_api"
      
      self._structure = {
        f"{self.request_base_url}/actual_generation/v1/" : ["actual_generations_per_production_type", "actual_generations_per_unit"],
        f"{self.request_base_url}/balancing_energy/v4/" : ["volumes_per_energy_type", "prices", "imbalance_data", "standard_rr_data", "lead_times", "afrr_marginal_price", "volumes_per_entity_price", "tso_offers", "standard_afrr_data", "volumes_per_reasons"]
         }
      
      self._mapping = {
            name: f"{prefix}{name}"
            for prefix, names in self._structure.items()
            for name in names
        }

    @property
    def keys(self) -> str:
        return list(self._mapping.keys())

    def get(self, key: str, default=None) -> str:
        return self._mapping.get(key, default)
      
    def to_markdown(self) -> str:
        md = []
        md.append("| *data_type* | Request URL (Base) |")
        md.append("|-------------------|-----|")
        for name, url in self._mapping.items():
            md.append(f"| `{name}` | *{url}* |")
        return "".join(md)

    def __repr__(self):
      _repr = "OpenRTE Catalog : \n"
      for i, (key, url) in enumerate(self._mapping.items()):
        _repr += f"{i} - {key} : {url} \n"
      return _repr
        
